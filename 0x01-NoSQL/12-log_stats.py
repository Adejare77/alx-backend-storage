#!/usr/bin/env python3
"""Log stats"""

from pymongo import MongoClient


def log_stats(log_collection):
    """provides some stats about Nginx logs stored in MongoDB"""
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    print(f'{log_collection.count_documents({})} logs')
    print('Methods:')
    for method in methods:
        count = log_collection.count_documents({"method": f'{method}'})
        print(f'\tmethod {method}: {count}')
    method_path = log_collection.count_documents(
        {
            "$and": [
                {"method": 'GET'},
                {"path": "/status"}
            ]
        }
    )

    print(f'{method_path} status check')


if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017')
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)
