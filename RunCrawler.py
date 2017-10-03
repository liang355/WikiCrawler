import wiki_crawler

# Input Parameters
SeedUrl = 'https://en.wikipedia.org/wiki/Gerard_Salton'
Numpages = 800

print(wiki_crawler.crawl_web(SeedUrl, Numpages))
