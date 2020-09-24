from sys import path
from query import Query
from client import solrClient
import pandas as pd
import re

punctuation ='!,;:?"\''
def removePunctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation), '', text)
    return text.strip().lower()

data_path = 'data/query_dev_pairs.csv'
querys = pd.read_csv(data_path)
client = solrClient()

for i in range(querys.shape[0]):
    query = querys.loc[i, :]
    qid = query['qid']
    query_fields = ['contents', 'len_label', 'readability']
    query_values = [removePunctuation(query['query_text']), query['sub_len_label'], query['sub_readability']]
    q = Query('field_query', qid, query_fields, query_values)
    client.get_results(q)
    print(f'{i} query processed.')

result_path = 'data/result.csv'
client.export_results(result_path)
