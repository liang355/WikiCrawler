# WikiSearchEngine
Wikipedia Search Engine From Scratch

The WikiSearchEngine has 3 major components:
1. A crawler: crawling Wikipedia pages from seed urls, and save crawled documents and urls in files
2. A transformer & indexer: 
  i.  tokenize all crawled HTML documents, and save tokens into a signle file separated by document names
  ii. scan through all the tokens, and create several index files including an inverted-index file
3. A ranked retrieval module: 
  i.  create APIs to query the index files
  ii. given a query, calculate cosine similarity score of each document, and return the top-k most similar documents
  
How to use:
1. run RunCrawler.py with arguments: 1) seed url and 2) number of pages to crawl
2. run CreateIndex.py, which will run transformer and then indexer, you need to specify 1) number of crawed documents to create index on
3. write down your queries in Queries.txt file, one query per line
4. run RunRankedRetrieval.py with 1) number of results you want to return for each query
