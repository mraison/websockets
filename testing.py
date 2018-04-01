import turtle
from mouse_interfaces import mouseClient


mouse = mouseClient()


def onDrag(x, y):
    turtle.ondrag(None)
    turtle.setposition(x,y)

    mouse.setRelPosition(x - mouse.x, y - mouse.y)
    mouse.setAbsolutePosition(x, y)
    mouse.action = mouse.MOVEREL

    turtle.ondrag(onDrag, 1, True)


def onLeftClick(x,y):
    print("L click");


def onRightClick(x,y):
    print("R click");


def onRelease(x,y):
    # print("Mouse absolute position = (%s, %s)" % (mouse.x, mouse.y))
    # print("Mouse differential position = (%s, %s)" % (mouse.relX, mouse.relY))
    turtle.setposition(0.0, 0.0)

    mouse.x = 0
    mouse.y = 0
    mouse.relX = 0
    mouse.relY = 0
    mouse.action = None


turtle.speed(10) # increase speed so turtle keeps up with mouse.
turtle.shapesize(8, 8, 8)

turtle.onclick(onLeftClick, 1, True)
turtle.onclick(onRightClick, 2, True)
turtle.ondrag(onDrag, 1, True)
turtle.onrelease(onRelease, 1, True)

turtle.done()
print('after steps')
print('blah')