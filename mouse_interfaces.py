import pyautogui
import json

class mouseClient(object):

    LEFTCLICK  = 'lclick'
    RIGHTCLICK = 'rclick'
    MOVEREL    = 'moverel'

    possibleActions = {
        LEFTCLICK: None,
        RIGHTCLICK: None,
        MOVEREL: None
    }

    def __init__(self):
        self.action = None
        self.x = 0
        self.y = 0
        self.relX = 0
        self.relY = 0
        # set up action collection
        self.possibleActions[self.RIGHTCLICK] = self.rightClick
        self.possibleActions[self.LEFTCLICK] = self.leftClick
        self.possibleActions[self.MOVEREL] = self.moveRel

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


    # functions for the server to use
    def moveRel(self, x, y):
        pyautogui.moveRel(x, y)


    def leftClick(self):
        pyautogui.click(button='left')


    def rightClick(self):
        pyautogui.click(button='right')


    def doAction(self, action):
        if action in [self.LEFTCLICK, self.RIGHTCLICK, self.MOVE]:
            self.possibleActions[action]()


    def setAction(self, action):
        if action in [self.LEFTCLICK, self.RIGHTCLICK, self.MOVE]:
            self.action = action


    # functions for the client to use
    def setRelPosition(self, x, y):
        self.relX = x
        # I may need to multiply the y by -1 just to make sure that it converts well to the mouse control on the client.
        self.relY = y


    def setAbsolutePosition(self, x, y):
        self.x = x
        self.y = y

