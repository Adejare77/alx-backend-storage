#!/usr/bin/env python3
"""Log stats"""

from pymongo import MongoClient


def log_stats():
    """provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://localhost:27017')
    log_collection = client.logs.nginx
    print(f'{log_collection.count_documents({})} logs')

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
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
    log_stats()
