import time
import board
import neopixel

red = (255, 0, 0, 0)
yellow = (255, 150, 0, 0)
green = (0, 255, 0, 0)
cyan = (0, 255, 255, 0)
blue = (0, 0, 255, 0)
purple = (180, 0, 255, 0)
white = (0, 255, 255, 255)
off = (0, 0, 0, 0)

pixel_pin = board.A1
num_pixels = 294

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.9, auto_write=False,
                           pixel_order=(1, 0, 2, 3))

def strobe(iterations,wait):
	for i in range(iterations):
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

def color_chase(color, wait, delay):
    for i in range(num_pixels):
		if i != num_pixels-1:
			pixels[i] = color
			time.sleep(wait)
			pixels.show()
		else:
			time.sleep(delay)