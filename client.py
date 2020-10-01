from io import RawIOBase
from operator import index
from types import coroutine
from pandas.core.algorithms import rank
import pysolr
import urllib3
import json
import pandas as pd
from query import Query


class solrClient(object):
    """
    main class for performing search with solr through pysolr.
    internal variables:
        solr : type of pysolr.Solr. solr instance that connected to remote solr server.
        results : search results dict.
            key: ['qid', 'pid','passage','len_label','readability','rank'].
            value: value for each key. 

    """

    def __init__(self, server_url='http://localhost', server_port='8983', server_core='msmarcoPassage'):
        self.server_url = server_url
        self.server_port = server_port
        self.server_core = server_core
        self.solr = pysolr.Solr(
            server_url + ':' + server_port + '/solr/' + server_core)

        self.results = {
            'qid': [],
            'pid': [],
            'passage': [],
            'len_label': [],
            'readability': [],
            'rank': [],
        }

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

    def preserve_results(self, query, results):
        """
        preserve search results into self.results.
        parameter:
            query : query for search.
            results : search results of type of pysolr.Result class.
        """
        qid = query.query['qid']
        if results.hits == 0:
            self.results['qid'].append(qid)
            self.results['pid'].append("Null")
            self.results['passage'].append("Null")
            #self.results['len_label'].append("Null")
            #self.results['readability'].append("Null")
            self.results['len_label'].append(query.query['len_label'])
            self.results['readability'].append(query.query['readability'])
            self.results['rank'].append("Null")
        
        rank = 1
        for result in results:
            self.results['qid'].append(qid)
            self.results['pid'].append(result['pid'][0])
            self.results['passage'].append(result['contents'][0])
            self.results['len_label'].append(result['len_label'][0])
            self.results['readability'].append(result['readability'])
            self.results['rank'].append(rank)
            rank += 1

    def get_results(self, query):
        """
        perform search using pysolr.Solr and preserve results self.results dict.
        parameter:
            query : query of Query class.

        """
        results = self.search(query, 1000)
        self.preserve_results(query, results)
        print('search query {0}'.format(query.query['qid']))
        print("found {0} result(s)".format(results.hits))
        print("-------------------------------------------------")

    def export_results(self, path):
        # export perserved results into local file.
        rs = pd.DataFrame(self.results)
        rs.to_csv(path, index=False)
