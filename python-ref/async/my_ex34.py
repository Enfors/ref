#!/usr/bin/env python3.6

"""
This is my own experiment for Python 3.4+.
"""

import asyncio

async def calc(number):
    print("Calculating", number, "times 2 (sleeping to simulate slow calc)")
    await asyncio.sleep(5)
    return number * 2

async def do_work(number):
    print("Starting to work with", number)
    # This is where the magic happens.
    # We will now wait (using the "await" keyword) for calc(number) to finish.
    # But the thing is, while we do that, the program will NOT simply sleep!
    # It will be doing OTHER tasks from the tasks list below.
    new_number = await calc(number)
    print(number, "times 2 is", new_number)

tasks = [
    asyncio.ensure_future(do_work(2)),
    asyncio.ensure_future(do_work(4)),
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

                        
