import WikiCrawler

# Input Parameters
SeedUrl = 'https://en.wikipedia.org/wiki/Gerard_Salton'
Numpages = 80

print(WikiCrawler.crawl_web(SeedUrl, Numpages))
