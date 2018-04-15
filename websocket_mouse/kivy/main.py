import kivy

kivy.require('1.0.9')
from kivy.app import App
from kivy.uix.behaviors import DragBehavior
from kivy.uix.scatterlayout import ScatterLayout
from websocket_mouse.mouseController import mouseController

class MouseLayout(DragBehavior, ScatterLayout):
    mouse = mouseController()

    def leftClick(self, x, y):
        self.mouse.onLeftClick()

    def rightClick(self, x, y):
        self.mouse.onRightClick()

    def move(self, x, y):
        pass


class MouseApp(App):
    def build(self):
        return MouseLayout()
    #     return FloatLayout()


calcApp = MouseApp()
calcApp.run()
# print(LoggerHistory.history)