

import turtle
import math


class Fish:
	def __init__(self):
		self.turtle = turtle.Turtle()
		self.turtle.up()
		self.turtle.hideturtle()
		self.turtle.shape("Fish.gif")

		self.xpos = 0
		self.ypos = 0
		self.world = None

		self.breedTick = 0


	def setX(self, newX):
		self.xpos = newX


	def setY(self, newy):
		self.ypos = newy


	def getX(self):
		return self.xpos


	def getY(self):
		return self.ypos


	def setWorld(self, aworld):
		self.world = aworld


	def appear(self):
		self.turtle.goto(self.xpos, self.ypos)
		self.turtle.showturtle()


	def hide(self):
		self.turtle.hideturtle()


	def move(self, newx, newy):
		self.world.moveThing(self.xpos, self.ypos, newx, newy)
		self.xpos = newx 
		self.ypos = newy
		self.turtle.goto(self.xpos, self.ypos)


	def liveALittle(self):
		offsetList = [(-1,1),(0,1),(1,1),
						(-1,0),		(1,0),
						(-1,-1),(0,-1),(1,-1)]

		adjfish = 0
		for offset in offsetList:
			newx = self.xpos + offset[0]
			newy = self.ypos + offset[1]
			if 0 <= newx < self.world.getMaxX() and 0 <= newy < self.world.getMaxY():
				if (not self.world.emptyLocation(newx, newy)) and isinstance(self.world.lookAtLocation(newx, newy), Fish):
					adjfish = adjfish + 1

		if adjfish >= 2:
			self.world.delThing(self)
		else:
			self.breedTick = self.breedTick + 1
			if self.breedTick >= 12:
				self.tryToBreed()

			self.tryToMove()


	def tryToBreed(self):
		offsetList = [(-1,1),(0,1),(1,1),
						(-1,0),		(1,0),
						(-1,-1),(0,-1),(1,-1)]
		randomOffsetIndex = random.randrange(len(offsetList))
		randomOffset = offsetList[randomOffsetIndex]
		nextx = self.xpos + randomOffset[0]
		nexty = self.ypos + randomOffset[1]

		while not (0 <= nextx < self.world.getMaxX() and 0 <= nexty < self.world.getMaxY()):
			randomOffsetIndex = random.randrange(len(offsetList))
			randomOffset = offsetList[randomOffsetIndex]
			nextx = self.xpos + randomOffset[0]
			nexty = self.ypos + randomOffset[1]

		if self.world.emptyLocation(nextx, nexty):
			childThing = Fish()
			self.world.addThing(childThing, nextx, nexty)
			self.breedTick = 0


	def tryToMove(self):
		offsetList = [(-1,1),(0,1),(1,1),
						(-1,0),		(1,0),
						(-1,-1),(0,-1),(1,-1)]			
		randomOffsetIndex = random.randrange(len(offsetList))
		randomOffset = offsetList[randomOffsetIndex]
		nextx = self.xpos + randomOffset[0]
		nexty = self.ypos + randomOffset[1]

		while not (0 <= nextx < self.world.getMaxX() and 0 <= nexty < self.world.getMaxY()):
			randomOffsetIndex = random.randrange(len(offsetList))
			randomOffset = offsetList[randomOffsetIndex]
			nextx = self.xpos + randomOffset[0]
			nexty = self.ypos + randomOffset[1]

		if self.world.emptyLocation(nextx, nexty):
			self.move(nextx, nexty)









