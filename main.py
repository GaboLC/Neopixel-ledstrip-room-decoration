import time
import board
import neopixel

pixel_pin = board.A1
num_pixels = 294

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.9, auto_write=False,
                           pixel_order=(1, 0, 2, 3))

red = (255, 0, 0, 0)

while True:
	pixels.fill(red)
	pixels.show()