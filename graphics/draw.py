

import math
import turtle


class Canvas:
	def __init__(self, w, h):
		self.width = w
		self.height = h
		self.visibleObjects = []
		self.turtle = turtle.Turtle()
		self.screen = turtle.Screen()
		self.screen.setup(width = self.width, height = self.height)
		self.turtle.hideturtle()

	def drawAll(self):
		self.turtle.reset()
		self.turtle.tracer(0)
		for shape in self.visibleObjects:
			shape._draw(self.turtle)
		self.turtle.tracer(1)
		self.turtle.hideturtle()

	def addShape(self, shape):
		self.visibleObjects.append(shape)

	def draw(self, gObject):
		gObject.setCanvas(self)
		gObject.setVisible(True)
		self.turtle.up()
		self.screen.tracer(0)
		gObject._draw(self.turtle)
		self.screen.tracer(1)
		self.addShape(gObject)



class GeometricObject:
	def __init__(self):
		self.lineColor = 'black'
		self.lineWidth = 1
		self.visible = False
		self.myCanvas = None

	def setColor(self, color):
		self.lineColor = color
		if self.visible:
			self.myCanvas.drawAll()

	def setWidth(self, width):
		self.lineWidth = width
		if self.visible:
			self.myCanvas.drawAll()

	def getColor(self):
		return self.lineColor

	def getWidth(self):
		return self.lineWidth

	def _draw(self, someturtle):
		print("Error: You must define _draw in subclass")

	def setVisible(self, vFlag):
		self.visible = vFlag

	def setCanvas(self, theCanvas):
		self.myCanvas = theCanvas



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


	












