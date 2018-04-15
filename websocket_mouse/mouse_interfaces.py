class mouseInt(object):

    # things they both need

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


    # State control
    def setRelPosition(self, x, y):
        self.relX = x
        # I may need to multiply the y by -1 just to make sure that it converts well to the mouse control on the client.
        self.relY = y

    def setAbsolutePosition(self, x, y):
        self.x = x
        self.y = y


    def reset(self):
        self.x = 0
        self.y = 0
        self.relX = 0
        self.relY = 0
        self.action = None



