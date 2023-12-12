#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
import random


async def async_generator():
    """
    Asynchronous generator that yields ten
    random numbers between 0 and 10.

    This generator asynchronously yields a random
    float between 0 and 10 every second.
    It does this for ten iterations, making use of
    asyncio's sleep function to
    demonstrate asynchronous behavior.

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
