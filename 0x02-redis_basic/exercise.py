#!/usr/bin/env python3
"""Writing strings to Redis"""

import redis
import uuid
from typing import Union


class Cache:
    """store an instance of Redis client as private variable named _redis
    and flush the instance using flushdb
    """
    def __init__(self) -> None:
        """initialize the instance database and flush"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store the input data in Redis using the random key
        and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
