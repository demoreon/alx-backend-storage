#!/usr/bin/env python3

from pymongo import MongoClient

def log_stats():
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    total = logs_collection.count_documents({})
    get = logs_collection.count_documents({"method": "GET"})
    post = logs_collection.count_documents({"method": "POST"})
    put = logs_collection.count_documents({"method": "PUT"})
    patch = logs_collection.count_documents({"method": "PATCH"})
    delete = logs_collection.count_documents({"method": "DELETE"})
    path = logs_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{total} logs")
    print("\tmethod GET: {get}")
    print("\tmethod POST: {post}")
    print("\tmethod PUT: {put}")
    print("\tmethod PATCH: {patch}")
    print("\tmethod DELETE: {delete}")
    print(f"{path} status check")

    if __name__ == "__main__":
        log_stats()
