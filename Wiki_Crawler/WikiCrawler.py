import urllib2
import sys

# Constants:
MAX_LEVEL = 5


# get the next target link in the given page content
def get_next_link(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote+1)
    url = page[start_quote + 1: end_quote]
    string_url = ''.join(url)
    host = 'https://en.wikipedia.org'
    # validate url by checking pattern
    if url is None:
        return None, 0
    if url[:6] == '/wiki/' and ':' not in url[6:]:
        url = host + url
    if url[:len(host)] != host:
        url = None
    if 'Main_Page' in string_url:
        url = None
    return url, end_quote


# make HTTP call and get the page content from the given URL
def get_page(link):
    user_agent = 'macOS/10.12.6'
    headers = {'User-Agent': user_agent}
    req = urllib2.Request(link, headers=headers)
    size = 0
    try:
        source_file = urllib2.urlopen(req)
        source_text = source_file.read()
        size = sys.getsizeof(source_text)
    except:
        print('invalid url requested')
        return ''
    return source_text, size


# append q to p and remove duplicates
def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


# get all HTML links in the given page by shrinking page size at each iteration
def get_all_links(page):
    lists = []
    while True:
        url, endpos = get_next_link(page)
        if endpos != 0:
            if url is not None:
                lists.append(url)
            page = page[endpos:]
        else:
            break
    return lists


# BFS crawling to keep track of level:
def crawl_web(seed, numpages):
    f = open("URLsCrawled.txt", "w")
    to_crawl = [seed]
    crawled = []
    max_size = -1
    min_size = sys.maxsize
    size_sum = 0
    level = 0
    while to_crawl and len(crawled) < numpages and level <= MAX_LEVEL:
        temp_list = []
        level = level + 1
        # dequeue all links at current level
        while to_crawl and len(crawled) < numpages and level <= MAX_LEVEL:
            link = to_crawl.pop(0)
            page, size = get_page(link)
            if page != '' and link not in crawled:  # ignore invalid links and crawled pages
                # write current page to file
                crawled_file = open("CrawledPages/file" + str(len(crawled) + 1) + ".txt", "w")
                crawled_file.write(page)
                if size > max_size:
                    max_size = size
                if size < min_size:
                    min_size = size
                size_sum += size
                crawled.append(link)
                f.write(link + '\n')
                union(temp_list, get_all_links(page))
                print("Current Page", link, 'count = ' + str(len(crawled)), 'level = ' + str(level), 'size = ' + str(size))
        # enqueue all links at next level
        union(to_crawl, temp_list)
    f.close()
    # write stat variables to Stats.txt
    file_stats = open("Stats.txt", "w")
    file_stats.write('Maximum size: ' + str(max_size) + ' bytes\n')
    file_stats.write('Minimum size: ' + str(min_size) + ' bytes\n')
    file_stats.write('Average size: ' + str(size_sum / len(crawled)) + ' bytes\n')
    file_stats.write('Maximum depth reach: ' + str(level) + '\n')
    file_stats.close()
    return crawled
