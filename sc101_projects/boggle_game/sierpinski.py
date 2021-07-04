"""
File: sierpinski.py
Name: Livia Tseng 曾迺芩
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	Draw a sierpinski_triangle in given orders.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	This function draws the sierpinski triangle recursively.
	:param order: Decide how many different size of triangle on the canvas.
	:param length: The length of side of the biggest triangle.
	:param upper_left_x: x of upper left point of the biggest triangle.
	:param upper_left_y: y of upper left point of the biggest triangle.
	:return: Sierpinski triangle on the canvas.
	"""
	if order == 0:
		pass
	else:
		upper_l = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
		left_l = GLine(upper_left_x, upper_left_y, upper_left_x+length/2, upper_left_y+length*0.866)
		right_l = GLine(upper_left_x+length, upper_left_y, upper_left_x+length/2, upper_left_y+length*0.866)
		window.add(upper_l)
		window.add(left_l)
		window.add(right_l)
		# Left
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)
		# Right
		sierpinski_triangle(order-1, length/2, upper_left_x+length/2, upper_left_y)
		# Bottom
		sierpinski_triangle(order-1, length/2, upper_left_x+length/4, upper_left_y+length/2*0.866)


if __name__ == '__main__':
	main()