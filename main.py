from lights import *

pixel_pin = board.A1
num_pixels = 294

while True:
	color_chase(red, 0.0001, 5)
	color_chase(yellow, 0.0001, 5)
	color_chase(green, 0.0001, 5)
	color_chase(cyan, 0.0001, 5)
	color_chase(blue, 0.0001, 5)
	color_chase(purple, 0.0001, 5)
	strobe(10, 0.5, 30)