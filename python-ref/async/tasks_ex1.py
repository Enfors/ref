#!/usr/bin/env python3.6

"""
This example is taken from
https://www.blog.pythonlibrary.org/2016/07/26/python-3-an-intro-to-asyncio/.
"""

import asyncio

async def my_task(seconds):
    """
    A task to do for a number of seconds.
    """
    print("This task is taking {} seconds to complete".format(seconds))
    await asyncio.sleep(seconds)
    return "task finished"


if __name__ == "__main__":
    my_event_loop = asyncio.get_event_loop()

    try:
        print("Task creation started.")
        task_obj = my_event_loop.create_task(my_task(seconds=2))
        my_event_loop.run_until_complete(task_obj)

    finally:
        my_event_loop.close()

    print("The task's result was: {}".format(task_obj.result()))

        
