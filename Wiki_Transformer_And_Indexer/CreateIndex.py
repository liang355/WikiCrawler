from WikiIndexer import create_index
from RunDataTransformer import run_transformer


# input params
FolderName = "CrawledPages"
NumFilesToProcess = 60
Filename = 'Out/Tokens.txt'

run_transformer(FolderName, NumFilesToProcess)
create_index(Filename)
