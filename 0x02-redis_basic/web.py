#!/usr/bin/env python3
"""Display implement a get_page function"""
import requests
import redis
import time


class Cache:
    def __init__(self):
        """Display cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def count_calls(self, func):
        def wrapper(*args, **kwargs):
            key = f"count:{args[0]}"
            self._redis.incr(key)
            return func(*args, **kwargs)
        return wrapper

    def cache(self, ttl):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                key = f"cache:{args[0]}"
                if self._redis.exists(key):
                    return self._redis.get(key)
                else:
                    result = func(*args, **kwargs)
                    self._redis.setex(key, ttl, result)
                    return result
            return wrapper
        return decorator


class Web:
    def __init__(self):
        self.cache = Cache()

    @self.cache.count_calls
    @self.cache.cache(ttl=10)
    def get_page(self, url):
        response = requests.get(url)
        time.sleep(3)
        return response.content.decode()
