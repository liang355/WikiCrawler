import os

import WikiCrawler

# move up current working directory by one level
os.chdir('..')

# Input Parameters
SeedUrl = 'https://en.wikipedia.org/wiki/Gerard_Salton'
NumPages = 800

print(WikiCrawler.crawl_web(SeedUrl, NumPages))
