#!/usr/bin/env python
from MouseClick import MouseClick
import os

def main():
	os.system("clear")
	print("Left click the positions required, then right click when your finished.")
	clicks = MouseClick()
	clicks.run()


	print(clicks.left_clicks)


if __name__ == '__main__':
	main()