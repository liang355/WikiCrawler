import os
import sys
import re
import math
import operator

from UseIndex import get_term_id_by_term
from UseIndex import get_freq_by_term_id_doc_id
from UseIndex import get_doc_ids_by_term
from UseIndex import get_doc_by_doc_id

# Global variables:
print os.getcwd()
N = sum(1 for line in open('../IndexFiles/DocumentIDFile.txt')) - 1  # total number of indexed documents


def read_raw_queries(queries_file):
    with open('Wiki_Ranked_Retrieval/' + queries_file, 'r') as read_f:
        return read_f.read().split('\n')


def tokenize_query(raw_query):
    tokens = re.findall(r'[\w]+', raw_query)
    return tokens


def tf_idf(term, doc_id):
    # print term, doc_id
    term_id = get_term_id_by_term(term)
    raw_tf = get_freq_by_term_id_doc_id(term_id, doc_id)
    # print raw_tf
    if raw_tf is None:
        return 0
    tf = int(raw_tf)
    df = len(get_doc_ids_by_term(term))
    return math.log10(1 + tf) * math.log10(N / df)


def tf_idf_from_query(term, query):
    tf = 0
    for token in query:
        if term == token:
            tf = tf + 1
    df = 1
    return math.log10(1 + tf) * math.log10(N / df)


def get_doc_snippet(doc_id, docs_folder):
    doc = get_doc_by_doc_id(doc_id)
    with open(docs_folder + '/' + doc, 'r') as read_f:
        snippet = read_f.read(200)
        return snippet


def top_k_results(query_tokens, k, docs_folder):
    # query vector (also its normalized factor)
    query_vector = []
    query_length = 0
    for term in query_tokens:
        entry = tf_idf_from_query(term, query_tokens)
        query_vector.append(entry)
        query_length += entry ** 2
    query_length = math.sqrt(query_length)

    # doc vectors and cosine scores (also their normalized factors)
    scores = {}
    contributions = {}
    for doc_id in range(0, N):
        doc_id = str(doc_id)
        doc_vector = []
        doc_length = 0
        for term in query_tokens:
            entry = tf_idf(term, doc_id)
            doc_vector.append(entry)
            doc_length += entry ** 2
        doc_length = math.sqrt(doc_length)
        # sum up the cosine score factors for current doc_id
        score = 0
        products = {}
        for q, d, term in zip(query_vector, doc_vector, query_tokens):
            score += q * d
            products[term] = q * d
        # normalize cosine score
        total_length = query_length * doc_length
        normalized_score = score / float(total_length) if total_length != 0 else 0

        # for print
        scores[doc_id] = normalized_score
        contributions[doc_id] = products

    # sort cosine scores
    sorted_scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
    top_k_scores = sorted_scores if len(sorted_scores) <= k else sorted_scores[0:k]

    # construct results
    results = ''
    for tuple in top_k_scores:
        # data to print
        doc_id = tuple[0]
        doc = get_doc_by_doc_id(doc_id)
        snippet = get_doc_snippet(doc_id, docs_folder)
        score = scores[doc_id]
        contribution = contributions[doc_id]

        # get contribution_string
        pairs = []
        for term, product in contribution.iteritems():
            pair = term + ': ' + str(product)
            pairs.append(pair)
        contribution_string = '; '.join(pairs)

        # construct result string
        result = ''
        result += doc_id + '\t' + doc + '\n'
        result += snippet + '\n'
        result += 'cosine score: ' + str(score) + '\n'
        result += contribution_string + '\n\n'
        results += result

    return results


def retrieve_ranked_docs(index_folder, docs_folder, queries_file, k):
    with open('Wiki_Ranked_Retrieval/Output.txt', 'w') as write_f:
        raw_queries = read_raw_queries(queries_file)
        for raw_query in raw_queries:
            query_tokens = tokenize_query(raw_query)
            write_f.write(raw_query + '\n')
            write_f.write(str(query_tokens) + '\n')
            write_f.write(top_k_results(query_tokens, k, docs_folder) + '\n\n\n')

