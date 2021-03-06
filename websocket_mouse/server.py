#!/usr/bin/env python

import asyncio
import websockets
import pyautogui
from mouse_interface_for_server import mouseServerInt
pyautogui.FAILSAFE = False

class websocketServer(object):

    def __init__(self):
        self.host = '0.0.0.0'
        self.port = 8765
        self.mouseCli = mouseServerInt()


    def run(self):
        print('running...')
        async def mouseControl(websocket, path):
            message = await websocket.recv()
            self.mouseCli.loadFromJson(message)
            ## do action
            self.mouseCli.doAction()
            self.mouseCli.action = None
            await websocket.send("recieved")

        asyncio.get_event_loop().run_until_complete(websockets.serve(mouseControl, self.host, self.port))
        asyncio.get_event_loop().run_forever()



server = websocketServer()
server.run()