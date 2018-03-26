#!/usr/bin/env python

import asyncio
import websockets
from mouse_interfaces import mouseClient

class websocketServer(object):

    def __init__(self):
        self.host = '0.0.0.0'
        self.port = 8765
        self.mouseCli = mouseClient()
        self._setActions()


    def run(self):
        print('running...')
        async def echo(websocket, path):
            message = await websocket.recv()
            ## do action
            self._doAction(message)

            await websocket.send("recieved")

        asyncio.get_event_loop().run_until_complete(websockets.serve(echo, self.host, self.port))
        asyncio.get_event_loop().run_forever()


    def _doAction(self, message):
        self.actions[message]()


    def _setActions(self):
        self.actions = {
            'move': self.mouseCli.moveRel,
            'lclick': self.mouseCli.leftClick,
            'rclick': self.mouseCli.rightClick
        }


server = websocketServer()
server.run()