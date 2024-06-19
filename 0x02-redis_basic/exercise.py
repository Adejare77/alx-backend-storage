#!/usr/bin/env python3
"""Writing strings to Redis"""

import redis
import uuid
from typing import Union, Optional, Callable


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

    def get(self, key, fn: Optional[Callable]=None) -> Union[str, bytes, int, float]:
        """takes a 'key' string argument and an optional Callable argument
        name 'fn'
        """
        if self._redis.get(key):
            value = self._redis.get(key)
            if fn:
                try:
                    result = self.get_int(value)
                except ValueError as e:
                    try:
                        result = self.get_float(value)
                    except Exception as e:
                        result = self.get_str(value)
                return result
            return value

    def get_str(self, key):
        """parametrize Cache.get to string data type"""
        return key.decode('utf-8')

    def get_int(self, key):
        """parametrize Cache.get to int data type"""
        value = key.decode('utf-8')
        return int(value)

    def get_float(self, key):
        """parametrize Cache.get to float data type"""
        value = key.decode('utf-8')
        return float(value)
