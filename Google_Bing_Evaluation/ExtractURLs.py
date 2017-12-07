import os
from bs4 import BeautifulSoup


def get_result_links_from_all_pages(folder, flag):
    all_links = []
    for filename in os.listdir(folder):
        filepath = folder + '/' + filename
        links = get_links_from_result_page(filepath, flag)
        all_links.append(links)
    return all_links


def get_links_from_result_page(filename, flag):
    with open(filename, 'r') as read_f:
        soup = BeautifulSoup(read_f, 'html.parser')
        links = []
        if flag == 'Google':
            target_tag = 'h3'
        else:
            target_tag = 'h2'
        for tag in soup.find_all(target_tag):
            a_tag = tag.find('a')
            if a_tag is not None:
                link = a_tag.get('href')
                if link[0:4] == 'http':
                    links.append(link)
        if len(links) > 10:
            return links[1:]
        return links


def get_google_bing_result_links():
    with open('GoogleURLs.txt', 'w') as write_file:
        google_results = get_result_links_from_all_pages("SearchResultPages/GoogleResults", 'Google')
        for results in google_results:
            for result in results:
                print result
                write_file.write(result + '\n')
            write_file.write('\n')
            print ''

    with open('BingURLs.txt', 'w') as write_file:
        google_results = get_result_links_from_all_pages("SearchResultPages/BingResults", 'Bing')
        for results in google_results:
            for result in results:
                print result
                write_file.write(result + '\n')
            write_file.write('\n')
            print ''


get_google_bing_result_links()
# print get_links_from_bing_result_page('SearchResultPages/BingResults/BingSearch_Query1_1.htm')
