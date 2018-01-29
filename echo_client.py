#!/usr/bin/env python

import asyncio
import websockets

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        send_txt = "hello world"
        print(send_txt)
        await websocket.send(send_txt)

        recieve_txt = await websocket.recv()
        print(recieve_txt)


# I ~think~ you want to put 0.0.0.0 as this is the "default" placeholder...
# I believe what this will tell the server to listen on whatever port.
# The outward facing port just happens to by your external IP but putting 0.0.0.0 will just say "listen for whatever."
asyncio.get_event_loop().run_until_complete(
    hello('ws://192.168.1.4:8765'))