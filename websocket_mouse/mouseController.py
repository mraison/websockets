from websocket_mouse.mouse_interfaces_for_client import mouseClientInt
from websocket_mouse.client import websocketClient


class mouseController(object):

    def __init__(self):
        self.ws = websocketClient()
        self.mouse = mouseClientInt()


    def onDrag(self, x, y):
        self.mouse.setRelPosition(x - self.mouse.x, y - self.mouse.y)
        self.mouse.setAbsolutePosition(x, y)
        self.mouse.setAction(self.mouse.MOVE)
        self.ws.run(self.mouse.serialize())

        self.mouse.reset()


    def onLeftClick(self, x,y):
        self.mouse.setRelPosition(x - self.mouse.x, y - self.mouse.y)
        self.mouse.setAbsolutePosition(x, y)
        self.mouse.setAction(self.mouse.LEFTCLICK)
        self.ws.run(self.mouse.serialize())

        self.mouse.reset()
        print("L click");


    def onRightClick(self, x,y):
        self.mouse.setRelPosition(x - self.mouse.x, y - self.mouse.y)
        self.mouse.setAbsolutePosition(x, y)
        self.mouse.setAction(self.mouse.RIGHTCLICK)
        self.ws.run(self.mouse.serialize())

        self.mouse.reset()
        print("R click");


    def onRelease(self, x,y):
        self.mouse.reset()
