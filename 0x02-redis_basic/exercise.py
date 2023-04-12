#!/usr/bin/env python3
"""Display Create a Cache class. In the __init__ method"""
from typing import Callable, Optional, Union
from uuid import uuid4
import redis
from functools import wraps


class Cache:
    def __init__(self):
        """Return the key"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
