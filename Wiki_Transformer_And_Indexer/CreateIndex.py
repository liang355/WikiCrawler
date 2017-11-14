import os
from WikiIndexer import create_index
from WikiTransformer import transform_data

# move up current working directory by one level
os.chdir('..')


# input params
CrawledDocsFolder = "CrawledPages"
NumFilesToProcess = 60
Filename = 'IndexFiles/Tokens.txt'

transform_data(CrawledDocsFolder, NumFilesToProcess)
create_index(Filename)
