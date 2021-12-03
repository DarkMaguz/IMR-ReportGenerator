import os
import sys
from datetime import timedelta
from flask import Flask, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename
import asyncio
# from quart import websocket
# from quart_trio import QuartTrio
from flask_socketio import SocketIO, emit

sys.path.append('imr')
from imr import imr

app = Flask(__name__)
socketio = SocketIO(app)

app.config['UPLOAD_EXTENSIONS'] = ['.xlsx' ]
app.config['UPLOAD_DIR'] = 'uploaded'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 10


@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process')
def process():
  return render_template('process.html')


@app.route('/processing')
def processing():
  #async with trio.open_nursery() as nursery:
  #
  #imr()
  return render_template('processing.html')


@app.route('/', methods=['POST'])
def upload_file():
    myFiles = request.files
    for item in myFiles:
        uploadedFile = myFiles.get(item)
        uploadedFile.filename = secure_filename(uploadedFile.filename)
        if uploadedFile.filename != '':
            fileExt = os.path.splitext(uploadedFile.filename)[-1]
        if fileExt not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploadedFilePath = os.path.join(app.config['UPLOAD_DIR'], uploadedFile.filename)
        uploadedFile.save(uploadedFilePath)
    return redirect(url_for('process'))


if __name__ == '__main__':
  socketio.run(app, debug=True, host='0.0.0.0', port=5001)
  #app.run(debug=True, host='0.0.0.0', port=5001)
