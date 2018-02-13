import sys
import os
import requests

class Client(object):
    """A simple API client for the Xray's API.
    see README for more details
    """


    tests_name = []
    test_suites = []
    #last_update = 89    


    
    def __init__(self, api_token=None, url_base=""):
        self.api_token = api_token
        self.vars = "" #["startUrl" : "http://google.com",... ]
        self.url_base = url_base

###

    def _request(self, path, parameters=None):

        data = requests.get("%s%s?apiKey=%s" % (self.url_base, path, self.api_token))
        print("%s%s?apiKey=%s" % (self.url_base, path, self.api_token))
        return data.json()


###EXTRAS

    def get_id_by_test_name(self, testid):
        """
        """
        response = self._request("tests/<testId>/")
        print(response)
        return response
   
    def get_test_by_name(self, test_name):
        """
        """ 
        id = self.get_id_by_test_name(test_name)
        self.get_test_by_id(id)
        response = self._request("tests/<testId>/")
        print(response)
        return response

###TESTS

    def get_test_by_id(self, testid):
        """ 
        """
        response = self._request("tests/<testId>/")
        print(response)
        return response

    def get_tests(self):
        """
        """
        response = self._request("tests/")
        print(response)
        return response

###TESTS_SUITES

    def get_test_suites(self):
        """
        """
        response = self._request("tests/")
        print(response)
        return response

    def get_test_suite(self):
        """
        """
        response = self._request("tests/")
        print(response)
        return response
    

###TESTS_RESULTS

    def get_suite_results_by_results_id(self, id):
        """
        """
        print("get_test_results")
        response = self._request("tests/")
        print(response)
        return response

    def get_results_id(self, id):
        """
        """
        print("get_test_results")
        response = self._request("tests/")
        print(response)
        return response
    

###TESTS_EXUCUTIONS
        
    def run_test(self):
        """
        """
        response = self._request("tests/")
        print(response)
        return response
    