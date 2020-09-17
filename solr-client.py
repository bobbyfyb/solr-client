import pysolr
import urllib3

from query import Query
# Server Information
server_url = 'http://localhost'
server_port = '8983'
server_core = 'msmarcoPassage'

# Query
query_fields = ['contents', 'len_label', 'readability']
query_values = ['what is paula deen\'s brother', 'equal', 'diffcult']
query = Query('field_query', 2, query_fields, query_values)
print(query.get_query_string())

# Connection
# http://localhost:8983/solr/msmarco/select?q=
solr = pysolr.Solr(
    server_url + ':' + server_port +
    '/solr/' + server_core
)
# Search and response
results = solr.search(query.get_query_string(), **{"rows":1000})
#results = solr.search("*:*")

""" print(results.hits)
print(results.__len__())
print(len(results.docs)) """

# Print the response
#print("Found {0} result(s).".format(len(results)))
#for result in results:
#    print(
#        f"{result['contents']} with length: {result['len_label']} and comlexicity {result['readability']}")

solr