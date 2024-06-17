#!/usr/bin/env python3
"""Lists all documents in a collection"""


# if __name__ == '__main__':
def list_all(mongo_collection):
    """returns documents in collections else []"""
    query = mongo_collection.find()
    return query
