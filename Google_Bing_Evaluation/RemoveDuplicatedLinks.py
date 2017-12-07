
def remove_duplilcates(read_file, write_file):
    all_links = []
    with open(read_file, 'r') as read_f:
        for line in read_f:
            if line != '':
                all_links.append(line)
    all_links = set(all_links)
    with open(write_file, 'w') as write_f:
        for link in all_links:
            write_f.write(link)
    return all_links


remove_duplilcates('Top15_RawLinks_Query1.txt', 'UniqueLinks_Query1.txt')
remove_duplilcates('Top15_RawLinks_Query2.txt', 'UniqueLinks_Query2.txt')
