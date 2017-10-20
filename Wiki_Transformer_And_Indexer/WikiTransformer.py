import os
import re
import sys
from bs4 import BeautifulSoup


def transform(folder_name, num_files_to_process):
    tokens_list = []
    total_files_size = 0
    tokens_count = 0
    with open('Out/Tokens.txt', 'w') as write_f:
        for filename in os.listdir(folder_name)[:num_files_to_process]:
            with open(folder_name + '/' + filename, 'r') as read_f:
                page = read_f.read()
                total_files_size += sys.getsizeof(page)

                # get content between <title> tags
                title_search = re.search('<title>(.*)</title>', page, re.IGNORECASE)
                if title_search:
                    title = re.sub('<[^<]+?>', '', title_search.group(1))
                else:
                    title = ''

                # remove <head> and <script> sections
                soup = BeautifulSoup(page, "lxml")
                for tag in soup.find_all('head'):
                    tag.replaceWith('')
                for tag in soup.find_all('script'):
                    tag.replaceWith('')
                cleaner_page = soup.get_text()

                # handles acronyms like I.B.M. to IBM
                # handles apostrophes
                cleaner_page.replace('.', '')
                cleaner_page.replace('\'', '')

                # tokens = cleaner_page.split()
                tokens = re.findall(r"[\w']+", cleaner_page)
                tokens_count += len(tokens)
                tokens_list += tokens
                cur_file = str(filename) + '\n'
                print(cur_file)
                write_f.write(cur_file)
                for token in tokens:
                    print token
                    write_f.write(token + '\n')

    # write to stats.txt
    s = set(tokens_list)
    unique_tokens_count = len(s)
    with open('Out/stats.txt', 'w') as write_file:
        write_file.write('Total size of all the input files (in bytes): ' + str(total_files_size) + '\n')
        write_file.write('Total number of tokens: ' + str(tokens_count) + '\n')
        write_file.write('Total number of unique tokens: ' + str(unique_tokens_count) + '\n')

