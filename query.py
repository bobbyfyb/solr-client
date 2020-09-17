import pysolr
import urllib3
import json


class Query(object):


    """
    Query class for wrapping query to search in solr.
    internal variables:
        query_string: 'q' string paramters for query.
        encoded_query: query of json format.

    Agument:
        query_type : label to decide query types. either 'standard' or 'field query'.
        query_id : integer. indicates query id.
        query_fields : List. indicates which fields will be used.
        query_values : List of same length with query fields. indicates each field value.

    """

    def __init__(self, query_type='standard', query_id=None,  query_fields=None, query_values=None):
        self.query = self.encoded_query(query_id, query_fields, query_values)
        if query_type == 'standard':
            self.query_string = self.standard_query(query_fields, query_values)
        elif query_type == 'field_query':
            self.query_string = self.field_query(query_fields, query_values)
        else:
            self.query_string == None

    def standard_query(self, query_fields, query_values):
        query = query_fields + ":" + query_values
        # print(query)
        return query

    def field_query(self, query_fields, query_values):
        query = ""
        for field, value in zip(query_fields, query_values):
            query += "+" + field + ":" + value + "\n"
        # print(query)
        return query

    def get_query_string(self):
        return self.query_string

    def encoded_query(self, query_id, query_fields, query_values):
        q = {'qid': query_id}
        for field, value in zip(query_fields, query_values):
            q[field] = value
        encoded_query = json.dumps(q)
        return encoded_query

    def get_encoded_query(self):
        return self.query

# query = Query('standard', 'contents', 'Androgen receptor define')
# print(query.get_query())

""" field_query = Query('field_query', 2, ['contents', 'len_label', 'readability'], [
                    'Androgen receptor define', 'equal', 'difficult'])
print(field_query.get_query_string())
 """
