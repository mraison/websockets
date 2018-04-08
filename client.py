#!/usr/bin/env python

import asyncio
import websockets

class websocketClient(object):

    def __init__(self):
        self.host = '192.168.1.13'
        self.port = '8765'


    def run(self, message):
        async def send(uri, message):
            async with websockets.connect(uri) as websocket:
                await websocket.send(message)

                recieve_txt = await websocket.recv()
                print(recieve_txt)



        # I ~think~ you want to put 0.0.0.0 as this is the "default" placeholder...
        # I believe what this will tell the server to listen on whatever port.
        # The outward facing port just happens to by your external IP but putting 0.0.0.0 will just say "listen for whatever."
        asyncio.get_event_loop().run_until_complete(
            send('ws://' + self.host + ':' + self.port, message)
        )


# cli = websocketClient()
# cli.run()