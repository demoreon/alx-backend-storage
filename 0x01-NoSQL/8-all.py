#!/usr/bin/env python3
"""
List all documents in collection
"""


def list_all(mongo_collection):
    """
    function to list document in a collection

    :param mongo_collection:
    :return:
    """
    return mongo_collection.find()
