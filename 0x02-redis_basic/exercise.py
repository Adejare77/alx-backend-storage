#!/usr/bin/env python3
"""Writing strings to Redis"""

import redis
import uuid
import functools
from typing import Union, Optional, Callable


def count_calls(method: Callable) -> Callable:
    """Decorator to count calls to the method."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Callable:
        """preserve the original metadata and return the wrapper"""
        # Generate a custom key
        # key = f"{self.__class__.__name__}.{method.__name__}"
        key = method.__qualname__
        # Increment the count for this method
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs of a method"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """preserve the original metadata and return the wrapper"""
        input_key = f"{self.__class__.__name__}.{method.__name__}:inputs"
        output_key = method.__qualname__ + ":outputs"

        # store the input arguments
        self._redis.rpush(input_key, str(args))

        # call the original method and store its output
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return str(output)
    return wrapper


class Cache:
    """store an instance of Redis client as private variable named _redis
    and flush the instance using flushdb
    """
    def __init__(self) -> None:
        """initialize the instance database and flush"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store the input data in Redis using the random key
        and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn: Optional[Callable] =
            None) -> Union[str, bytes, int, float]:
        """takes a 'key' string argument and an optional Callable argument
        name 'fn'
        """
        if self._redis.get(key):
            value = self._redis.get(key)
            if fn:
                try:
                    result = self.get_int(value)
                except ValueError as e:
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


def replay(method: Callable) -> None:
    """Display the history of calls of a particular function."""
    redis_client = method.__self__._redis
    inputs_key = method.__qualname__ + ":inputs"
    outputs_key = method.__qualname__ + ":outputs"

    inputs = redis_client.lrange(inputs_key, 0, -1)
    outputs = redis_client.lrange(outputs_key, 0, -1)

    call_count = len(inputs)
    print(f"{method.__qualname__} was called {call_count} times:")
    for input_args, output in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(method.__qualname__,
                                     input_args.decode('utf-8'),
                                     output.decode('utf-8')))
