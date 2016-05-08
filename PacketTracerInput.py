#!/usr/bin/env python
from PyUserInputCustom.pymouse.x11 import PyMouse, PyMouseEvent
from PyUserInputCustom.pykeyboard.x11 import PyKeyboard
from MouseClick import MouseClick
import time
import os

class PacketTracerInput:
	'''Makes it easier for a user to make a PC's IP config in PT easier. Instead of having to go
	through each PC and typing the info, they will enter the IP's here info in this program, the
	program will the go through each pc assigning the info to each PC'''
	def __init__(self, primary_butn=1):
		self.coords = []
		self.primary_butn = primary_butn

	def get_coords(self):
		m = MouseClick(btn=self.primary_butn)
		m.run()
		self.coords = m.clicks
		return self.coords

def main():
	os.system("clear")

if __name__ == '__main__':
	main()