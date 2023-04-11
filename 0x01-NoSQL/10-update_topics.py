#!/usr/bin/env python3
"""Display changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Define changes"""
    result = mongo_collection.update_many(
      {"name": name},
      {"$set": {"topics": topics}}
    )

    return result.modified_count
