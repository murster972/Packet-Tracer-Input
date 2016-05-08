from PyUserInputCustom.pymouse.x11 import PyMouse, PyMouseEvent
import os

class MouseClick(PyMouseEvent):
	def __init__(self, btn=1):
		''':param click_number: number of button presses to get from mouse'''
		PyMouseEvent.__init__(self)
		self.clicks = []
		self.btn = btn

	def click(self, x, y, button, press):
		#records a click mutliple times if press is not checked
		if button == self.btn:
			if press:
				print(x, y)
				self.clicks.append((x, y))
		else: self.stop()

	def run(self):
		"""print("***Make sure this window is not in the way.")
		print("Please make sure the approptiate window is open and you are able to click the positions.***")
		print("click on each position - with the approptiate button - required, then right or middle click when finished")
		"""raw_input("Press any key to start...")
		PyMouseEvent.run(self)