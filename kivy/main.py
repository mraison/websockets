import kivy
kivy.require('1.0.9')
from kivy.app import App
from kivy.uix.label  import Label
from kivy.uix.behaviors import DragBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.scatterlayout import ScatterLayout
from kivy.logger import Logger, LoggerHistory


class MouseLayout(DragBehavior, ScatterLayout):
    def leftClick(self):
        # Logger.info('left click.')
        pass

    def rightClick(self):
        # Logger.info('right click.')
        pass

    def move(self):
        pass


class MouseApp(App):
    def build(self):
        return MouseLayout()
    #     return FloatLayout()


calcApp = MouseApp()
calcApp.run()
# print(LoggerHistory.history)