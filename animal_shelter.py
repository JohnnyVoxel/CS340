"""
Shaun Ryan
CS-340 Client/Server Development
22EW1
10/02/2022
"""

from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint
from bson.json_util import dumps

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username="aacuser", password="aacpass"):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('localhost:56367')
        self.database = self.client.AAC
        self.database.authenticate(username, password, source='AAC')

    # Create method
    def create(self, data):
        if data is not None:
            if 'animal_id' in data:
                if self.database.animals.insert(data):  # data should be dictionary
                    return True  # data successfully inserted
                else:
                    return False  # data not inserted
            else:
                return False  # no key values were passed in the dictionary
        else:
            raise Exception("Nothing to save, because data parameter is empty.")

    # Read method
    def read(self, query):
        if query is not None:
            results = self.database.animals.find(query, {"_id": 0})  # find results of query
            if results.count() != 0:
                #for document in results:  # iterate through the results
                #    pprint(document)  # output the results
                return results
            else:
                return False  # no results found
        else:
            raise Exception("No search parameter entered.")
        return results

    # Update method
    def update(self, query, data):
        if len(query.keys()) >= 1:
            if self.database.animals.count(query) != 0:
                update = self.database.animals.update_many(query, {"$set": data})
                return update.raw_result
            else:
                return False
        else:
            raise Exception("No search parameter entered.")

    # Delete method
    def delete(self, query):
        if len(query.keys()) >= 1:
            if self.database.animals.count(query) != 0:
                result = self.database.animals.delete_many(query)
                return result.raw_result
            else:
                return False
        else:
            raise Exception("No search parameter entered.")