import os
import sys

import validators
import concurrent.futures

import settings as cfg
import utils
import downloader as dler
import excel

def worker(dataPoint):
	dataPair = []
	for url in dataPoint['URLs']:
		isOK = False
		isURL = validators.url(url) == True
		fileName = ''
		responseCode = 0
		mimeType = ''
		if isURL:
			fileName = utils.getFileName(url)
			responseCode = dler.getFile(url, fileName)
			if 200 <= responseCode <= 299:
				mimeType = utils.getMimeType(fileName)
				isOK = utils.isPDF(mimeType)
			if not isOK:
				utils.cleanup(fileName)
		dataPair.append({
			'url': url,
			'isOK': isOK,
			'isURL': isURL,
			'fileName': fileName,
			'responseCode': responseCode,
			'mimeType': mimeType
		})
		if isOK:
			break
	dataPoint['dataPair'] = dataPair
	return dataPoint


def setup():
	if not os.path.exists(cfg.dataSouceDir):
		print('Could not find "data" directory!')
		sys.exit(1)
	if not os.path.exists(cfg.downloadDir):
		os.makedirs(cfg.downloadDir)


def main():
	setup()
	excelFiles = utils.getExcelFiles()
	dataPoints = []
	for file in excelFiles:
		dataPoints += excel.loadURLs(file)
	print('found %d rows of data points' % (len(dataPoints)))
	reports = []
	# We can use a with statement to ensure threads are cleaned up promptly
	with concurrent.futures.ProcessPoolExecutor(max_workers=cfg.maxWorkers) as executor:
		# Start the worker operations and mark each future with its URL
		future_to_dp = {executor.submit(worker, dp): dp for dp in dataPoints}
		for future in concurrent.futures.as_completed(future_to_dp):
			dp = future_to_dp[future]
			try:
				dataPoint = future.result()
			except Exception as e:
				print('%r generated an exception: %s' % (dp['BRN'], e))
			else:
				reports.append(dataPoint)
	excel.writeReport(reports)


if __name__ == '__main__':
	with utils.MyTimer():
		main()
