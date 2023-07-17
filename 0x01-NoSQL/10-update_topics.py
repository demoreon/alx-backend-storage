#!/usr/bin/env python3
"""
Change school topics based on name
"""


def update_topics(mongo_collection, name, topics):
    """
    function to alter a document based on name

    :param mongo_collection:
    :param name:
    :param topics:
    :return:
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
