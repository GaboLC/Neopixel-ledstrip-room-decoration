import time
import board
import neopixel

pixel_pin = board.A1
num_pixels = 294

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.9, auto_write=False,
                           pixel_order=(1, 0, 2, 3))

red = (255, 0, 0, 0)
yellow = (255, 150, 0, 0)
green = (0, 255, 0, 0)
cyan = (0, 255, 255, 0)
blue = (0, 0, 255, 0)
purple = (180, 0, 255, 0)
white = (0, 255, 255, 255)
off = (0, 0, 0, 0)

def strobe(wait):
	pixels.fill(red)
	pixels.show()
	time.sleep(wait)

	pixels.fill(yellow)
	pixels.show()
	time.sleep(wait)

	pixels.fill(green)
	pixels.show()
	time.sleep(wait)

	pixels.fill(cyan)
	pixels.show()
	time.sleep(wait)

	pixels.fill(blue)
	pixels.show()
	time.sleep(wait)

	pixels.fill(purple)
	pixels.show()
	time.sleep(wait)

def color_chase(color, wait):
    for i in range(num_pixels):
		pixels[i] = color
		time.sleep(wait)
		pixels.show()

while True:
	color_chase(red, 0.0001)
	time.sleep(5)
	color_chase(yellow, 0.0001)
	time.sleep(5)
	color_chase(green, 0.0001)
	time.sleep(5)
	color_chase(cyan, 0.0001)
	time.sleep(5)
	color_chase(blue, 0.0001)
	time.sleep(5)
	color_chase(purple, 0.0001)
	time.sleep(5)
	strobe(0.5)
