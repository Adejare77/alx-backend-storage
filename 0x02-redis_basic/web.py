#!/usr/bin/env python3
"""Redis Basic"""

import redis
import requests
import functools
from typing import Callable


# Initialize the Redis client
redis_client = redis.Redis()


def count(method: Callable) -> Callable:
    """tracks how many times a particular URL was accessed"""
    @functools.wraps(method)
    def wrapper(url: str, *args, **kwargs):
        key = f'count:{url}'
        redis_client.incr(key)
        return method(url, *args, **kwargs)
    return wrapper


@count
def get_page(url: str) -> str:
    """Implementing an expiring web cache and tracker"""
    cache_key = f'cache:{url}'

    # checks if the key was already cached
    if redis_client.get(cache_key):
        # Decode the value since it'll be in bytes
        return redis_client.get(cache_key).decode('utf-8')

    resp = requests.get(url)

    # cache the result with an expiration time of 10 seconds
    redis_client.setex(cache_key, 10, resp.text)

    return resp.text


# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/3000/url/http://www.google.com"
    print(get_page(url))
    print(get_page(url))
