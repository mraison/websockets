import turtle
from mouse_interfaces import mouseInt
from client import websocketClient


class mouseController(object):

    def __init__(self):
        self.ws = websocketClient()
        self.mouse = mouseInt()


    def onDrag(self, x, y):
        self.mouse.setRelPosition(x - self.mouse.x, y - self.mouse.y)
        self.mouse.setAbsolutePosition(x, y)
        self.mouse.setAction(self.mouse.MOVE)
        self.ws.run(self.mouse.serialize())

        self.mouse.setRelPosition(0, 0)
        self.mouse.action = None


    def onLeftClick(self, x,y):
        self.mouse.setRelPosition(x - self.mouse.x, y - self.mouse.y)
        self.mouse.setAbsolutePosition(x, y)
        self.mouse.setAction(self.mouse.LEFTCLICK)
        self.ws.run(self.mouse.serialize())

        self.mouse.setRelPosition(0, 0)
        self.mouse.action = None
        print("L click");


    def onRightClick(self, x,y):
        self.mouse.setRelPosition(x - self.mouse.x, y - self.mouse.y)
        self.mouse.setAbsolutePosition(x, y)
        self.mouse.setAction(self.mouse.RIGHTCLICK)
        self.ws.run(self.mouse.serialize())

        self.mouse.setRelPosition(0, 0)
        self.mouse.action = None
        print("R click");


    def onRelease(self, x,y):
        self.mouse.reset()
