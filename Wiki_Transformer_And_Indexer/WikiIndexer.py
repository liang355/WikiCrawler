import re
import sys
from collections import Counter


def create_index(filename):
    with open(filename, 'r') as read_f:
        # read file
        text = read_f.read()
        # get each document name
        docs = re.findall(r'file.*\.txt\n', text)
        docs[:] = [doc[:len(doc) - 1] for doc in docs]
        # group/split tokens by document name
        parts = re.split(r'file.*\.txt\n', text)
        parts = parts[1:len(parts)]
        # open output file as write mode
        term_file = open('Out/TermIDFile.txt', 'w')
        doc_file = open('Out/DocumentIDFile.txt', 'w')
        inverted_file = open('Out/InvertedIndex.txt', 'w')

        # create <term, frequency>, <termid, term>, <doc, length>, <docid, doc> map and inverted_index map
        term_freq_map = {}
        termid_term_map = {}
        term_termid_map = {}
        doc_len_map = {}
        docid_doc_map = {}
        inverted_map = {}
        termid = 0
        docid = 0
        for part, doc in zip(parts, docs):
            terms = re.split(r'\n', part)
            terms = terms[:len(terms) - 1]
            # for <term, frequency> map
            s = set(terms)
            for term in s:
                if term not in term_freq_map:
                    term_freq_map[term] = 1
                    termid_term_map[termid] = term
                    term_termid_map[term] = termid
                    termid += 1
                else:
                    term_freq_map[term] += 1
            # <term, count> map
            count_map = Counter(terms)
            for term, count in count_map.iteritems():
                term_id = term_termid_map[term]
                if term_id not in inverted_map:
                    inverted_map[term_id] = []
                inverted_map[term_id].append([docid, count_map[term]])

            doc_len_map[doc] = len(terms)
            docid_doc_map[docid] = doc
            docid += 1

        # print and write data structures to files
        term_file.write('TermID, Term, Freq\n')
        for termid in termid_term_map:
            print(termid, termid_term_map[termid], term_freq_map[termid_term_map[termid]])
            term_file.write(str(termid) + ', ' + termid_term_map[termid] + ', ' + str(term_freq_map[termid_term_map[termid]]) + '\n')
        doc_file.write('DocID, Doc, Len\n')
        for docid in docid_doc_map:
            print(docid, docid_doc_map[docid], doc_len_map[docid_doc_map[docid]])
            doc_file.write(str(docid) + ', ' + docid_doc_map[docid] + ', ' + str(doc_len_map[docid_doc_map[docid]]) + '\n')
        inverted_file.write('TermID, Postings(DocID, Freq)\n')
        for termid in inverted_map:
            postings = inverted_map[termid]
            post_str_list = []
            for posting in postings:
                posting_str = '[' + ','.join(str(e) for e in posting) + ']'
                post_str_list.append(posting_str)
            postings_str = '[' + ';'.join(post_str_list) + ']'
            print(termid, postings_str)
            inverted_file.write(str(termid) + ', ' + postings_str + '\n')

        # close files
        term_file.close()
        doc_file.close()
        inverted_file.close()

        # write to stats.txt
        with open('Out/TermIDFile.txt', 'r') as read_term_file:
            data = read_term_file.read()
            term_file_size = sys.getsizeof(data)
            indices = data.split('\n')
            term_index_size = len(indices) - 2
        with open('Out/DocumentIDFile.txt', 'r') as read_doc_file:
            data = read_doc_file.read()
            doc_file_size = sys.getsizeof(data)
            indices = data.split('\n')
            doc_index_size = len(indices) - 2
        with open('Out/InvertedIndex.txt', 'r') as read_inverted_file:
            data = read_inverted_file.read()
            inverted_file_size = sys.getsizeof(data)
            indices = data.split('\n')
            inverted_index_size = len(indices) - 2
        total_index_file_size = term_file_size + doc_file_size + inverted_file_size
        total_index_size = term_index_size + doc_index_size + inverted_index_size
        print(total_index_file_size)
        with open('Out/stats.txt', 'a') as append_stats_file:
            append_stats_file.write('Total size of the three index files (in bytes): ' + str(total_index_file_size) + '\n')
            append_stats_file.write('Ratio of the index size to the total file size: ' + str(total_index_size / (total_index_file_size * 1.0)))

