from sys import path
from query import Query
from client import solrClient
import pandas as pd
import re
import os

punctuation ='\d)@#$%&*.!,;:?"\''
def removePunctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation), '', text)
    return text.strip().lower()

#client = solrClient()
querys = []

data_path = '~/playground/projects/fangyubo/pyserini/collections/querys/'
result_path = '~/playground/projects/fangyubo/pyserini/runs/results/'
n = 10
            
for i in range(n):
    querys.append(pd.read_csv(f"{data_path}querys{i}.csv"))

j = 0
processed = 0
for query_batch in querys:
    client = solrClient()
    sub_querys = query_batch
    for i in range(sub_querys.shape[0]):
        query = sub_querys.loc[i, :]
        qid = query['qid']
        query_fields = ['contents', 'len_label', 'readability']
        query_values = [removePunctuation(query['query_text']), query['sub_len_label'], query['sub_readability']]
        q = Query('field_query', qid, query_fields, query_values)
        try:
            client.get_results(q)
            #print(f'{i} query processed.')
            #client.export_results(f"{result_path}result{j}.csv")
        except:
            continue
    client.export_results(f"{result_path}result{j}.csv")
    processed += sub_querys.shape[0]
    j += 1
    print(f"{processed} queries processed.")

#result_path = '~/playground/projects/fangyubo/pyserini/runs/result.csv'
#client.export_results(result_path)
