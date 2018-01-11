

import math
import turtle


class Canvas:
	def __init__(self, w, h):
		self.turtle = turtle.Turtle()
		self.screen = turtle.Screen()
		self.width = w
		self.height = h

		self.screen.setup(width = self.width, height = self.height)
		self.turtle.hideturtle()

	def draw(self, gObject):
		self.turtle.up()
		self.screen.tracer(0)
		gObject._draw(self.turtle)
		self.screen.tracer(1)


class GeometricObject:
	def __init__(self):
		self.lineColor = 'black'
		self.lineWidth = 1

	def getColor(self):
		return self.lineColor

	def getWidth(self):
		return self.lineWidth

	def setColor(self, color):
		self.lineColor = color

	def setWidth(self, width):
		self.lineWidth = width

	def _draw(self, someturtle):
		print("Error: You must define _draw in subclass")


class Point(GeometricObject):
	def __init__(self, x, y):
		super().__init__()
		self.x = x
		self.y = y

	def getCoord(self):
		return (self.x, self.y)

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def _draw(self, turtle):
		turtle.goto(self.x, self.y)
		turtle.dot(self.lineWidth, self.lineColor)


class Line(GeometricObject):
	def __init__(self, p1, p2):
		super().__init__()
		self.p1 = p1
		self.p2 = p2

	def getP1(self):
		return self.p1

	def getP2(self):
		return self.p2

	def _draw(self, turtle):
		turtle.color(self.getColor())
		turtle.width(self.getWidth())
		turtle.goto(self.p1.getCoord())
		turtle.down()
		turtle.goto(self.p2.getCoord())


	












