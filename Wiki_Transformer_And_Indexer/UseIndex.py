# APIs for using index
def get_term_id_by_term(term):
    with open('Out/TermIDFile.txt', 'r') as read_file:
        data = read_file.read()
        items = data.split('\n')
        items = items[1:len(items) - 1]
        for item in items:
            fields = item.split(', ')
            if term == fields[1]:
                return fields[0]
        return None


def get_inverted_list_by_term_id(termid):
    with open('Out/InvertedIndex.txt', 'r') as read_file:
        data = read_file.read()
        items = data.split('\n')
        items = items[1:len(items) - 1]
        for item in items:
            fields = item.split(', ')
            if termid == fields[0]:
                return fields[1]
        return None


def get_doc_id_by_term(term):
    termid = get_term_id_by_term(term)
    inverted_list = get_inverted_list_by_term_id(termid)
    inverted_list = inverted_list[1:len(inverted_list) - 1]
    postings = inverted_list.split(';')
    doc_id_list = []
    for post in postings:
        post = post[1:len(post) - 1]
        pair = post.split(',')
        doc_id_list.append(pair[0])
    return doc_id_list


def get_doc_by_doc_id(doc):
    with open('Out/DocumentIDFile.txt', 'r') as read_file:
        data = read_file.read()
        items = data.split('\n')
        items = items[1:len(items) - 1]
        for item in items:
            fields = item.split(', ')
            if doc == fields[0]:
                return fields[1]
        return None


def get_docs_by_query(query):
    doc_id_list = get_doc_id_by_term(query)
    doc_list = []
    for doc_id in doc_id_list:
        doc = get_doc_by_doc_id(doc_id)
        doc_list.append(doc)
    return doc_list


print('Testing APIs...')
print(get_term_id_by_term('Chicago'))
print(get_inverted_list_by_term_id('6365'))
print(get_doc_id_by_term('Chicago'))
print(get_doc_by_doc_id('23'))
print('')

# executing query
QueryTerm = 'Chicago'
with open('README.txt', 'a') as write_file:
    print('Executing query \'' + QueryTerm + '\'...')
    for doc in get_docs_by_query(QueryTerm):
        print(doc)
        write_file.write(doc + '\n')
