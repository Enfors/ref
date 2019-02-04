#!/usr/bin/env python3.7

import asyncio

"""
This time we will have two things running concurrently.
"""


async def do_something(wait: int, arg: str):
    """
    Sleep for the specified number of seconds, then print the arg.
    """

    await asyncio.sleep(wait)
    print(arg)

async def main():
    """
    Create two tasks, and await their completion.
    """

    task1 = asyncio.create_task(do_something(3, "first"))
    task2 = asyncio.create_task(do_something(4, "second"))

    await task2
    await task1

asyncio.run(main())
