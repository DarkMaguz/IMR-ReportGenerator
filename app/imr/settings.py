import os
import datetime

baseDir = os.path.abspath('.')

dataSouceDir = os.path.join(baseDir, 'uploaded')

outputDir = os.path.join(baseDir, 'output')
metadataFile = os.path.join(outputDir, 'metadata.xlsx')
jsonFile = os.path.join(outputDir, 'log.json')
downloadDir = os.path.join(outputDir, 'downloaded')

print('now: ', str(datetime.datetime.now()))
print('baseDir:', baseDir)
print('dataSouceDir:', dataSouceDir)
print('outputDir:', outputDir)
print('metadataFile:', metadataFile)
print('jsonFile:', jsonFile)
print('downloadDir:', downloadDir)

for dir in [outputDir, downloadDir, dataSouceDir]:
    os.makedirs(dir, exist_ok=True)

# maxURLs: None or number grater than or eaqual to 2.
maxURLs = None
# minURLs: 2 or number less than or eaqual to maxURLs.
minURLs = 2

maxWorkers = 500
