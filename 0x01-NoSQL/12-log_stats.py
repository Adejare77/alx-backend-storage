#!/usr/bin/env python3
"""Log stats"""

from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """
    Prototype: def log_stats(mongo_collection, option=None):
    Provide some stats about Nginx logs stored in MongoDB
    """
    items = {}
    if option:
        value = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {value}")
        return

    result = mongo_collection.count_documents(items)
    print(f"{result} logs")
    print("Methods:")
    for method in METHODS:
        log_stats(nginx_collection, method)
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")


# def log_stats(log_collection):
#     """provides some stats about Nginx logs stored in MongoDB"""
#     methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

#     print(f'{log_collection.count_documents({})} logs')
#     print('Methods:')
#     for method in methods:
#         count = log_collection.count_documents({"method": f'{method}'})
#         print(f'\tmethod {method}: {count}')
#     method_path = log_collection.count_documents(
#         {
#             "$and": [
#                 {"method": 'GET'},
#                 {"path": "/status"}
#             ]
#         }
#     )

#     print(f'{method_path} status check')


if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017')
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)
