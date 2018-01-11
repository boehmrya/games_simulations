
import turtle
import math
from fish import *
from bear import *


class World:
	def __init__(self, mx, my):
		self.maxX = mx
		self.maxY = my
		self.thingList = []
		self.grid = []

		for arow in range(self.maxY):
			row = []
			for acol in range(self.maxY):
				row.append(None)
			self.grid.append(row)

		self.wturtle = turtle.Turtle()
		self.wscreen = turtle.Screen()
		self.wscreen.setworldcoordinates(0, 0, self.maxX - 1, self.maxY - 1)
		self.wscreen.addshape("Bear.gif")
		self.wscreen.addshape("Fish.gif")
		self.wturtle.hideturtle()


	def draw(self):
		self.wscreen.tracer(0)
		self.wturtle.forward(self.maxX - 1)
		self.wturtle.left(90)
		self.wturtle.forward(self.maxY - 1)
		self.wturtle.left(90)
		self.wturtle.forward(self.maxX - 1)
		self.wturtle.left(90)
		self.wturtle.forward(self.maxY - 1)
		self.wturtle.left(90)
		for i in range(self.maxY - 1):
			self.wturlte.forward(self.maxX - 1)
			self.wturtle.backward(self.maxX - 1)
			self.wturtle.left(90)
			self.wturtle.forward(1)
			self.wturtle.right(90)
		self.wturtle.forward(1)
		self.wturtle.right(90)
		for i in range(self.maxX - 2):
			self.wturlte.forward(self.maxY - 1)
			self.wturtle.backward(self.maxY - 1)
			self.wturtle.left(90)
			self.wturtle.forward(1)
			self.wturtle.right(90)
		self.wscreen.tracer(1)


	def freezeWorld(self):
		self.wscreen.exitonclick()


	def addThing(self, athing, x, y):
		athing.setX(x)
		athing.setY(y)
		self.grid[y][x] = athing
		athing.setWorld(self)
		self.thingList.append(athing)
		athing.appear()


	def delThing(self, athing):
		athing.hide()
		self.grid[athing.getY()][athing.getX()] = None
		self.thingList.remove(thing)


	def moveThing(self, oldx, oldy, newx, newy):
		self.grid[newy][newx] = self.grid[oldy][oldx]
		self.grid[oldy][oldx] = None


	def getMaxX(self):
		return self.maxX


	def getMaxY(self):
		return self.maxY


	def liveALittle(self):
		if self.thingList != []:
			athing = random.randrange(len(self.thingList))
			randomthing = self.thingList[athing]
			randomthing.liveALittle()


	def emptyLocation(self, x, y):
		if self.grid[y][x] == None:
			return True 
		else:
			return False


	def lookAtLocation(self, x, y):
		return self.grid[y][x]




def MainSimulation():
	numberOfBears = 10
	numberOfFish = 10
	worldLifeTime = 2500
	worldWidth = 50
	worldHeight = 25

	myworld = World(worldWidth, worldHeight)
	myworld.draw()

	for i in range(numberOfFish):
		newfish = Fish()
		x = random.randrange(myworld.getMaxX())
		y = random.randrange(myworld.getMaxY())
		while not myworld.emptyLocation(x, y):
			x = random.randrange(myworld.getMaxX())
			y = random.randrange(myworld.getMaxY())
		myworld.addThing(newfish, x, y)

	for i in range(numberOfBears):
		newbear = Bear()
		x = random.randrange(myworld.getMaxX())
		y = random.randrange(myworld.getMaxY())
		while not myworld.emptyLocation(x, y):
			x = random.randrange(myworld.getMaxX())
			y = random.randrange(myworld.getMaxY())
		myworld.addThing(newbear, x, y)

	for i in range(worldLifeTime):
		myworld.liveALittle()

	myworld.freezeWorld()


MainSimulation()











