import pyautogui
import json
from mouse_interfaces import mouseInt

class mouseServerInt(mouseInt):
    # Things the server needs
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


    def loadFromJson(self, jsonConfig):
        m = json.loads(jsonConfig)
        self.action = m['action']
        self.x = m['x']
        self.y = m['y']
        self.relX = m['relX']
        self.relY = m['relY']


