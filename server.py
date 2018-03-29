#!/usr/bin/env python

import asyncio
import websockets
from mouse_interfaces import mouseClient

class websocketServer(object):

    def __init__(self):
        self.host = '0.0.0.0'
        self.port = 8765
        self.mouseCli = mouseClient()


    def run(self):
        print('running...')
        async def echo(websocket, path):
            message = await websocket.recv()
            ## do action
            self.mouseCli.doAction(message)

            await websocket.send("recieved")

        asyncio.get_event_loop().run_until_complete(websockets.serve(echo, self.host, self.port))
        asyncio.get_event_loop().run_forever()



server = websocketServer()
server.run()