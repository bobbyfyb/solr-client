from query import Query
from client import solrClient
import pandas as pd

querys = pd.read_csv('data/query_dev_pairs.csv')
client = solrClient()

for i in range(querys.shape[0]):
    query = querys.loc[i, :]
    qid = query['qid']
    query_fields = ['contents', 'len_label', 'readability']
    query_values = [query['query_text'], query['sub_len_label'], query['sub_readability']]
    q = Query('field_query', qid, query_fields, query_values)
    client.get_results(q)

client.export_results()
