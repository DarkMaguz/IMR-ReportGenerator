import pikepdf
import PyPDF2


# excelFileList = getExcelFiles()
# print(getURLsFromExcelFile(excelFileList[0]))

# info = downloadFile(
#	 "http://arpeissig.at/wp-content/uploads/2016/02/D7_NHB_ARP_Final_2.pdf")
#
# dlReports = [info]


def validatePDF(filePath):
	#print('validatePDF: ', filePath)
	return magic.from_file(filePath, mime=True)
	# try:
	#	 output = magic.from_file(filePath, mime=True).lower()
	#	 if "pdf" not in output:
	#		 return False
	# except Exception as e:
	#	 return False
	# else:
	#	 return True

def validatePDF_test2(fileName):
	isOK = ""
	checkData = []
	filePath = os.path.join(downloadDir, fileName)
	try:
		pdfFile = pikepdf.open(filePath)
		#meta = pdfFile.open_metadata()
		#checkData.append(meta.pdfa_status)
		#checkData.append(meta['xmp:CreatorTool'])
		#checkData.append(pdfFile.check())
		#checkData.append(len(pdfFile.pages))
		#print(pdfFile.pages)
		#if pdfFile.pages <= 0:
		#	raise "k"
		#print(meta.pdfa_status)
	except Exception as e:
		isOK = "False"
	else:
		isOK = "True"
	return [isOK, checkData]

def validatePDF_test1(fileName):
	isOK = ['', '']
	checkData = []
	filePath = os.path.join(downloadDir, fileName)
	try:
		pdfFile = pikepdf.open(filePath)
		#meta = pdfFile.open_metadata()
		#status = meta.pdfa_status
		#checkData = pdfFile.check()
		checkData.append(len(pdfFile.pages))
		#checkData = [check, meta, status]
		#print(pdfFile.pages)
		if len(pdfFile.pages) <= 0:
			raise "k"
		#print(meta.pdfa_status)
	except Exception as e:
		isOK[0] = 'NO'
	else:
		isOK[0] = 'YES'
	try:
		with open(filePath, 'rb') as pdfFileObj:
			pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
			if pdfReader.numPages <= 0:
				raise "k"
	except Exception as e:
		isOK[1] = 'NO'
	else:
		isOK[1] = 'YES'
	#print('%s:\n	%s	%s' % (fileName, isOK[0], isOK[1]))
	#print('%s	%s' % (isOK[0], isOK[1]))
	return [isOK, checkData]



# if __name__ == '__main__':
#	 downloadInfo('https://www.abertis.com/informeanual2016/assets/pdfs/abertis-2016-integrated-annual-report.pdf')
#	 #header = b'HTTP/1.1 200 OK\r\nDate: Sun, 28 Nov 2021 12:45:04 GMT\r\nServer: Apache\r\nLast-Modified: Mon, 08 Jan 2018 10:00:02 GMT\r\nAccept-Ranges: bytes\r\nContent-Length: 5092104\r\nX-Content-Type-Options: nosniff\r\nConnection: close\r\nContent-Type: application/pdf\r\nStrict-Transport-Security: max-age=31536000; includeSubDomains; preload;\r\nX-Frame-Options: SAMEORIGIN\r\nX-XSS-Protection: 1; mode=block\r\nSet-Cookie: HA_Abertis_CK=mia1rrwhlni; path=/; HttpOnly; Secure\r\n\r\n'
#	 #print(header.decode('iso-8859-1'))
#	 for name, value in headers.items():
#		 print('%s: %s' % (name, value))
