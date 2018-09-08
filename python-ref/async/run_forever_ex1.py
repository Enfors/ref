#!/usr/bin/env python3.6

"""
Example taken from
https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/
"""

import asyncio


async def work():
    while True:
        await asyncio.sleep(1)
        print("Task executed")

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(work())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing loop")
    loop.close()
