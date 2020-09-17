from query import Query
from client import solrClient
import pandas as pd

client = solrClient()
query_fields = ['contents', 'len_label', 'readability']
query_values = ['what is paula deen\'s brother', 'equal', 'diffcult']
query_values_two = ['Androgen receptor define', 'long', 'diffcult']
query = Query('field_query', 10485, query_fields, query_values)
query_two = Query('field_query',2, query_fields, query_values_two )

client.get_results(query)
client.get_results(query_two)

r = pd.DataFrame(client.results)