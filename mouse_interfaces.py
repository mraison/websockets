import pyautogui
import json

class mouseClient(object):

    # constants for binding.
    LEFTCLICK  = 'lclick'
    RIGHTCLICK = 'rclick'
    MOVE       = 'moverel'

    # constant array for binding.
    possibleActions = {
        LEFTCLICK: None,
        RIGHTCLICK: None,
        MOVE: None
    }

    def __init__(self):
        self.action = None
        self.x = 0
        self.y = 0
        self.relX = 0
        self.relY = 0
        # set up action const:func binding
        self.possibleActions[self.RIGHTCLICK] = self.rightClick
        self.possibleActions[self.LEFTCLICK] = self.leftClick
        self.possibleActions[self.MOVE] = self.move

    def serialize(self):
        return json.dumps(
            {
                'x': self.x,
                'y': self.y,
                'relX': self.relX,
                'relY': self.relY,
                'action': self.action
            }
        )

    def loadFromJson(self, jsonConfig):
        m = json.loads(jsonConfig)
        self.action = m['action']
        self.x = m['x']
        self.y = m['y']
        self.relX = m['relX']
        self.relY = m['relY']


    def moveRel(self, x, y):
        pyautogui.moveRel(x, y)


    # Functions to be bound to mouse events...
    def move(self):
        self.moveRel(self.relX, self.relY)


    def leftClick(self):
        self.move() # add a move to keep position up to date
        pyautogui.click(button='left')


    def rightClick(self):
        self.move() # add a move to keep position up to date
        pyautogui.click(button='right')


    # Action managment
    def doAction(self):
        if self.action and self.action in [self.LEFTCLICK, self.RIGHTCLICK, self.MOVE]:
            self.possibleActions[self.action]()


    def setAction(self, action):
        if action in [self.LEFTCLICK, self.RIGHTCLICK, self.MOVE]:
            self.action = action


    # State control
    def setRelPosition(self, x, y):
        self.relX = x
        # I may need to multiply the y by -1 just to make sure that it converts well to the mouse control on the client.
        self.relY = y


    def setAbsolutePosition(self, x, y):
        self.x = x
        self.y = y

