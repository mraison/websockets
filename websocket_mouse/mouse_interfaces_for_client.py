import json
from websocket_mouse.mouse_interfaces import mouseInt


class mouseClientInt(mouseInt):
    # things the client needs
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


    def reset(self):
        self.x = 0
        self.y = 0
        self.relX = 0
        self.relY = 0
        self.action = None



