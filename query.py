import pysolr
import urllib3


class Query:
    def __init__(self, query_type='standard', query_fields=None, query_values=None):
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

    def get_query(self):
        return self.query_string


#query = Query('standard', 'contents', 'Androgen receptor define')
#print(query.get_query())

#field_query = Query('field_query', ['contents', 'len_label', 'readability'], [
#                    'Androgen receptor define', 'equal', 'difficult'])
#print(field_query.get_query())
