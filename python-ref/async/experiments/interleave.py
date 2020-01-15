#!/usr/bin/python3
"""
What happens if you interleave asynchronous functions with synchronous ones?
Turns out you can't.

Async functions can call ordinary ones, but ordinary ones can't call async ones.
"""

import asyncio


async def perform_task(message: str, delay: int):
    await asyncio.sleep(delay)
    print(f"Message after {delay} seconds: {message}")
    intermediate_func()

def intermediate_func():
    print("- Intermediate func")
    await leaf_task()

async def leaf_task():
    await asyncio.sleep(1)
    print("  - Leaf task")
    
async def main():
    tasks = []

    tasks.append(asyncio.create_task(perform_task("One", 2)))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
