from random import randint
from time import sleep
import sys
import pyttsx

FMT_STR = "{}\n\n{}\n\n--------------\n"

def speak(engine, what):
	engine.say(what)
	engine.runAndWait()

colors = ["red", "yellow", "blue", "green"]
directions = ["right", "left"]
body_part = ["hand", "foot"]

part_colors = [[None, None], [None, None]]

engine = pyttsx.init()

while True:
	while True:
		direction_int = randint(0,1)
		body_int = randint(0,1)
		color_int = randint(0,3)
		if part_colors[direction_int][body_int] != color_int:
			part_colors[direction_int][body_int] = color_int
			break
	
	appendage = directions[direction_int] + " " + body_part[body_int]
	color = colors[color_int]
	
	speak(engine, appendage + " " + color)
	
	print(FMT_STR.format(appendage, color))
	sleep(float(sys.argv[1]))
