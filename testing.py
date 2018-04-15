import turtle
from mouseController import mouseController
from client import websocketClient

ws = websocketClient()
mouse = mouseController()


def onDrag(x, y):
    turtle.ondrag(None)
    turtle.setposition(x,y)
    mouse.onDrag(x,y)

    turtle.ondrag(onDrag, 1, True)


def onLeftClick(x,y):
    mouse.onLeftClick(x,y)
    print("L click");


def onRightClick(x,y):
    mouse.onRightClick(x,y)
    print("R click");


def onRelease(x,y):
    turtle.setposition(0.0, 0.0)
    mouse.onRelease(x, y)


turtle.speed(10) # increase speed so turtle keeps up with mouse.
turtle.shapesize(8, 8, 8)

turtle.onclick(onLeftClick, 1, True)
turtle.onclick(onRightClick, 2, True)
turtle.ondrag(onDrag, 1, True)
turtle.onrelease(onRelease, 1, True)

turtle.done()
print('after steps')
print('blah')