#!/usr/bin/env python3.6

"""
Example taken from
https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/
"""

import asyncio
import time

# Define a coroutine that takes in a future
async def my_work():
    print("Starting work")
    time.sleep(5)
    print("Finishing work")

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(my_work())
finally:
    loop.close()
    
