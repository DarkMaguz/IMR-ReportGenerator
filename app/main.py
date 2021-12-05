import os
import sys
from flask import Flask, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO, emit
from multiprocessing import Process, Lock
import time

sys.path.append('imr')
import imr
import utils
import settings as cfg


app = Flask(__name__)
socketio = SocketIO(app, logger=True, async_mode='eventlet')


#app.config['SECRET_KEY'] = 'secret!'
app.config['UPLOAD_EXTENSIONS'] = ['.xlsx']
app.config['UPLOAD_DIR'] = 'uploaded'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 10

mainProcess = Process(target=imr.imr)


@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process')
def process():
    return render_template('process.html')


# @app.route('/processing')
# def processing():
#     emit('startedProcessing', 'k1')
#     mainProcess = Process(target=imr.imr)
#     p.start()
#
#     return render_template('processing.html')


@socketio.on('getState')
def handleGetState():
    global mainProcess
    if mainProcess.is_alive():
        if mainProcess.join(timeout=0.0001):
          emit('currentState', 'processing')
        else:
          emit('processingCompleted')
          emit('currentState', 'ready')
    else:
        if len(utils.getExcelFiles()) > 0:
            emit('currentState', 'ready')
        else:
            emit('currentState', 'sleeping')


@socketio.on('clearFiles')
def handleClearFiles():
    global mainProcess
    # if mainProcess:
    #   mainProcess.join()
    utils.cleanDir(cfg.outputDir)
    utils.cleanDir(cfg.dataSouceDir)
    emit('filesCleared')


@socketio.on('startProcessing')
def handleStartProcessing():
    global mainProcess
    mainProcess = Process(target=imr.imr)
    mainProcess.start()
    emit('startedProcessing')


@app.route('/', methods=['POST'])
def uploadFile():
    myFiles = request.files
    for item in myFiles:
        uploadedFile = myFiles.get(item)
        uploadedFile.filename = secure_filename(uploadedFile.filename)
        if uploadedFile.filename != '':
            fileExt = os.path.splitext(uploadedFile.filename)[-1]
        if fileExt not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploadedFilePath = os.path.join(
            app.config['UPLOAD_DIR'], uploadedFile.filename)
        uploadedFile.save(uploadedFilePath)
    return "", 202 #redirect(url_for('/'))



if __name__ == '__main__':
    print('Loading...')
    socketio.run(app, debug=True, host='0.0.0.0', port=5001)
    #app.run(debug=True, host='0.0.0.0', port=5001)
