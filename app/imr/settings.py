import os

baseDir = os.path.abspath('.')

dataSouceDir = os.path.join(baseDir, 'uploaded')

outputDir = os.path.join(baseDir, 'output')
metadataFile = os.path.join(outputDir, 'metadata.xlsx')
jsonFile = os.path.join(outputDir, 'log.json')
downloadDir = os.path.join(outputDir, 'downloaded')

print('baseDir:', baseDir)
print('dataSouceDir:', dataSouceDir)
print('outputDir:', outputDir)
print('metadataFile:', metadataFile)
print('jsonFile:', jsonFile)
print('downloadDir:', downloadDir)

# maxURLs: None or number grater than or eaqual to 2.
maxURLs = 5010
# minURLs: 2 or number less than or eaqual to maxURLs.
minURLs = 5000

maxWorkers = 5
