from PyUserInputCustom.pymouse.x11 import PyMouse, PyMouseEvent
from PyUserInputCustom.pykeyboard.x11 import PyKeyboard
import os

class TestClick(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)
        self.x = 0
        self.y = 0

    def click(self, x, y, button, press):
        if button == 1:
        	print(x, y)
        else: self.stop()

if __name__ == '__main__':
    os.system("clear")
    #tst = TestClick()
    #tst.run()

    PyMouse().click(972, 481, 1)
    PyKeyboard().type_string("Test Message.")