#!/usr/local/bin/python3.7

import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    #data = await reader.read(100)
    fut = reader.read(100)

    try:
        data = await asyncio.wait_for(fut, timeout=5)
    except asyncio.TimeoutError:
        print("Timeout. Aborting.")
        writer.close()
        return None

    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()

asyncio.run(tcp_echo_client('Hello World!'))
