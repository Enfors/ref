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
            print(response.status)
            return await response.read()

loop = asyncio.get_event_loop()

with aiohttp.ClientSession(loop=loop) as session:
    tasks = [
        asyncio.ensure_future(fetch_page(session,
                                         "http://python.org")),
        asyncio.ensure_future(fetch_page(session,
                                         "http://www.pythonvarmland.se"))
    ]
    
    loop.run_until_complete(asyncio.wait(tasks))
    
loop.close()
