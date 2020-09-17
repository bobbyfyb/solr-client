from io import RawIOBase
from types import coroutine
import pysolr
import urllib3
import json
import pandas as p
from query import Query


class solrClient(object):
    """
    main class for performing search with solr through pysolr.
    internal variables:
        solr : type of pysolr.Solr. solr instance that connected to remote solr server.
        results : search results dict of json format.
            key: query of Query class.
            value: related query results of json format.

    """

    def __init__(self, server_url='http://localhost', server_port='8983', server_core='msmarcoPassage'):
        self.server_url = server_url
        self.server_port = server_port
        self.server_core = server_core
        self.solr = pysolr.Solr(
            server_url + ':' + server_port + '/solr/' + server_core)

        self.results = {}

    def search(self, query, rows):
        """
        perform search through pysolr.
        parameter: 
            query: query of type Query class.
            rows: indicates the number of results needed.
        return:
            search results of type of pysolr.Results class.
        """
        return self.solr.search(query.get_query_string(), **{"rows": rows})

    def encode_results(self, results):
        """
        encode search results into json format.
        parameter:
            results : search results of type of pysolr.Result class.
        return:
            encoded results of json format.
        """
        encoded_results = []
        for result in results:
            r = {
                'pid': result['pid'],
                'contents': result['contents'],
                'len_label': result['len_label'],
                'readability': result['readability']
            }
            encoded_result = json.dumps(r)
            encoded_results.append(encoded_result)
        return encoded_results

    def get_results(self, query):
        """
        perform search using pysolr.Solr and preserve results of json format into self.results dict.
        parameter:
            query : query of Query class.
        return:
            results dict of perserved search results.

        """
        results = self.search(query, 1000)
        r = self.encode_results(results)
        self.results[query] = r
        print("found {0} result(s)".format(results.hits))
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("top 10 of found results:")
        top10_results = self.encode_results(self.search(query, 10))

        for r in top10_results:
            print(f"query : {query.get_encoded_query()}")
            print(r)
        return self.results

    def export_results(self):
        # TO DO://export perserved results into local file.
        pass