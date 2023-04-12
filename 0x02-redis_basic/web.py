#!/usr/bin/env python3
"""Display implement a get_page function"""
import redis
import requests
from typing import Callable
from functools import wraps

redis = redis.Redis()


def wrap_requests(fn: Callable) -> Callable:
    """Define wrapper"""

    @wraps(fn)
    def wrapper(url):
        """Wrapper"""
        redis.incr(f"count:{url}")
        cached_response = redis.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        result = fn(url)
        redis.setex(f"cached:{url}", 10, result)
        return result

    return wrapper


@wrap_requests
def get_page(url: str) -> str:
    """get"""
    response = requests.get(url)
    return response.text
