#!/usr/bin/env python3.6

"""
Example taken from
https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/
"""

import asyncio

# Define a coroutine that takes in a future
async def my_coroutine():
    print("My coroutine")


# Spin up a quick and simple event loop
# and run until completed
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(my_coroutine())
finally:
    loop.close()
    
