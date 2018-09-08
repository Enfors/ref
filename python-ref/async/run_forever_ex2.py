#!/usr/bin/env python3.6

"""
Example taken from
https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/
"""

import asyncio


async def first_worker():
    while True:
        await asyncio.sleep(1)
        print("First worker executed")


async def second_worker():
    while True:
        await asyncio.sleep(1)
        print("Second worker executed")

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(first_worker())
    asyncio.ensure_future(second_worker())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing loop")
    loop.close()
