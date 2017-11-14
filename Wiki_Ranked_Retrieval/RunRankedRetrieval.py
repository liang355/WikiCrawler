import os
from WikiRankedRetrieval import retrieve_ranked_docs
# move up current working directory by one level
os.chdir('..')

retrieve_ranked_docs('IndexFiles', 'CrawledPages', 'Queries.txt', 5)
