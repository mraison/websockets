#!/usr/bin/env python

import asyncio
import websockets
from mouse_interfaces import mouseClient


class websocketClient(object):

    def __init__(self):
        self.host = '192.168.1.13'
        self.port = '8765'
        self.mouse = mouseClient()


    def run(self):
        async def send(uri, action):
            async with websockets.connect(uri) as websocket:

                if action:
                    # print('sending...')
                    await websocket.send(action)

                    recieve_txt = await websocket.recv()
                    print(recieve_txt)



        # I ~think~ you want to put 0.0.0.0 as this is the "default" placeholder...
        # I believe what this will tell the server to listen on whatever port.
        # The outward facing port just happens to by your external IP but putting 0.0.0.0 will just say "listen for whatever."
        asyncio.get_event_loop().run_until_complete(
            send('ws://' + self.host + ':' + self.port, self.mouse.action)
        )
        self.mouse.action = None


cli = websocketClient()
cli.run()