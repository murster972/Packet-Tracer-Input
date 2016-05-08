#!/usr/bin/env 
from PacketTracerInput import PacketTracerInput
import os

def get_device_coords():
	pt_input = PacketTracerInput(primary_butn=2)
	return pt_input.get_coords()

def arg_count(cmd):
	total = 0
	for i in arg_count:
		total += 1 if i == '-s' else 0
	return total

def main():
	os.system("clear")
	commands = {}
	cmd = 1
	args = []

	while True:
		print("Enter command to be used, use '-s' to represent a variable value.")
		cmd = raw_input("Enter command: ")
		device = get_device_coords()

if __name__ == '__main__':
	main()