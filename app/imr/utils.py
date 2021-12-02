import os
import time
import magic

import settings as cfg

class MyTimer():
	def __init__(self):
		self.start = time.time()
	def __enter__(self):
		return self
	def __exit__(self, exc_type, exc_val, exc_tb):
		end = time.time()
		runtime = end - self.start
		msg = 'The function took {time} seconds to complete'
		print(msg.format(time=runtime))

def getExcelFiles():
	fileList = os.listdir(cfg.dataSouceDir)
	excelFileList = []
	for file in fileList:
		if file.endswith('.xlsx'):
			excelFileList.append(os.path.join(cfg.dataSouceDir, file))
	return excelFileList

def uniqueFile(fileName):
	filePath = os.path.join(cfg.downloadDir, fileName)
	if os.path.exists(filePath):
		fileName = uniqueFile(fileName.removesuffix('.pdf') + '_.pdf')
	return fileName

def genFileName(url):
	fileName = ''
	if url.startswith('https'):
		fileName = url.split('https://')[1].split('/')[0]
	else:
		if url.startswith('http'):
			fileName = url.split('http://')[1].split('/')[0]
		else:
			fileName = url.split('/')[0]
			fileName += '_G' + str(time.time())
	return fileName + '.pdf'

def getFileName(url):
	fileName = ''
	if url.lower().endswith('.pdf'):
		fileName = url.split('/')[-1]
	else:
		fileName = genFileName(url)
	return uniqueFile(fileName)

def getMimeType(fileName):
	filePath = os.path.join(cfg.downloadDir, fileName)
	if os.path.exists(filePath):
		return magic.from_file(filePath, mime=True)
	else:
		return ''

def isPDF(mimeType):
	return 'pdf' in mimeType.lower()

def cleanup(fileName):
	filePath = os.path.join(cfg.downloadDir, fileName)
	if os.path.isfile(filePath):
		try:
			os.remove(filePath)
		except Exception as e:
			print('cleanup() error removing file:', e)
