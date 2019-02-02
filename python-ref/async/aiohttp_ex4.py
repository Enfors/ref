#!/usr/bin/env python3.6

"""
Example from https://asyncio.readthedocs.io/en/latest/http_client.html
Adapted by Enfors
"""

import asyncio
import aiohttp

async def fetch_page(session, url):
    with aiohttp.Timeout(10):
        async with session.get(url) as response:
            assert response.status == 200
            content = await response.read()
            print(response.status, content[0:60])
            return content


loop = asyncio.get_event_loop()

with aiohttp.ClientSession(loop=loop) as session:

    tasks = list()

    for i in range(1, 100):
        tasks.append(
            asyncio.ensure_future(fetch_page(session,
                                             f"http://www.google.com?q={i}")))

    loop.run_until_complete(asyncio.wait(tasks))

loop.close()
