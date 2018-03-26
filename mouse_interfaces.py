import pyautogui;

class mouseClient(object):

    def moveRel(self, x, y):
        pyautogui.moveRel(x, y)

    def leftClick(self):
        pyautogui.click(button='left')

    def rightClick(self):
        pyautogui.click(button='right')