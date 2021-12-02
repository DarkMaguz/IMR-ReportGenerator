import os
import pycurl
import certifi
from io import BytesIO

import settings as cfg

def getHeader(url):
	header = BytesIO()
	try:
		curl = pycurl.Curl()
		curl.setopt(curl.URL, url)
		curl.setopt(curl.CAINFO, certifi.where())
		curl.setopt(curl.CONNECTTIMEOUT, 30)
		curl.setopt(curl.NOBODY, True)
		curl.setopt(curl.HEADERFUNCTION, header.write())
		curl.perform()
	except Exception as e:
		print('getHeader() error: %s' % (url, e))
	else:
		return header.getvalue().decode('iso-8859-1')
	finally:
		curl.close()

def getFile(url, fileName):
	responseCode = 0
	try:
		with open(os.path.join(cfg.downloadDir, fileName), 'wb') as pdfFile:
			curl = pycurl.Curl()
			curl.setopt(curl.URL, url)
			curl.setopt(curl.WRITEDATA, pdfFile)
			curl.setopt(curl.CAINFO, certifi.where())
			curl.setopt(curl.FOLLOWLOCATION, True)
			curl.setopt(curl.TIMEOUT, 300)
			curl.setopt(curl.LOW_SPEED_LIMIT, 5)
			curl.setopt(curl.CONNECTTIMEOUT, 30)
			curl.perform()
			responseCode = curl.getinfo(curl.RESPONSE_CODE)
			curl.close()
	except Exception as e:
		print('getFile() error: %s' % (url, e))
	finally:
		return responseCode
