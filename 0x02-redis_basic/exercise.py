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

    def get(self, key: str,
            fn: Callable = lambda x: x) -> Union[str, bytes, int, float, None]:
        if self._redis.exists(key):
            data = self._redis.get(key)
            return fn(data)
        else:
            return None

    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, lambda x: x.decode('utf-8')
                        if isinstance(x, bytes) else x)

    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, lambda x: int(x) if x is not None else x)


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def count_calls(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = func.__qualname__
            self._redis.incr(key)
            return func(*args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = lambda x: x) -> Union[str, bytes, int, float, None]:
        if self._redis.exists(key):
            data = self._redis.get(key)
            return fn(data)
        else:
            return None

    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, lambda x: x.decode('utf-8')
                        if isinstance(x, bytes) else x)

    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, lambda x: int(x) if x is not None else x)
