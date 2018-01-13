from turtle import Turtle,mainloop
import random
import math

class LaserCannon(Turtle):
    def __init__(self,xmin,xmax,ymin,ymax):
        super().__init__()
        self.screen = self.getscreen()
        self.screen.bgcolor('light green')
        self.screen.setworldcoordinates(xmin,ymin,xmax,ymax)
        self.screen.onclick(self.aim,1)
        self.screen.onkey(self.shoot,"s")
        self.screen.onkey(self.quit,'q')

    def aim(self,x,y):
        heading = self.towards(x,y)
        self.setheading(heading)

    def shoot(self):
        Bomb(self.heading(),5)
        
    def quit(self):
        self.screen.bye()
        
class BoundedTurtle(Turtle):
  def __init__(self, speed, xmin=-200,xmax=200,ymin=0,ymax=400):
      super().__init__()
      self.xmin = xmin
      self.xmax = xmax
      self.ymin = ymin
      self.ymax = ymax
      self.speed = speed

  def outOfBounds(self):
      xpos,ypos = self.position()
      out = False
      if xpos < self.xmin or xpos > self.xmax:
          out = True
      if ypos < self.ymin or ypos > self.ymax:
          out = True
      return out
        
  def move(self):
      self.forward(self.speed)
      if self.outOfBounds():
          self.remove()
      else:
          self.getscreen().ontimer(self.move,200)
            
  def remove(self):
      self.hideturtle()

        
class Bomb(BoundedTurtle):
    def __init__(self, initHeading,speed):
        super().__init__(speed)
        self.initHeading = initHeading
        self.resizemode('user')
        self.color('red','red')
        self.shape('circle')
        self.setheading(initHeading)
        self.up()
        self.turtlesize(.25)
        self.getscreen().ontimer(self.move,100)
        
    def move(self):
        exploded = False
        self.forward(self.speed)
        for i in Alien.getAliens():
            if self.distance(i) < 5:
                i.remove()
                exploded = True
        if self.outOfBounds() or exploded:
            self.remove()
        else:
            self.getscreen().ontimer(self.move,100)
            
    def distance(self,other):
        p1 = self.position()
        p2 = other.position()
        a = p1[0]-p2[0]
        b = p1[1]-p2[1]
        dist = math.sqrt(a**2 + b**2)
        return dist

    
class Alien(BoundedTurtle):
    alienList = []

    @staticmethod
    def getAliens():
        return [x for x in Alien.alienList if x.alive]  
        
    def __init__(self,speed,xmin,xmax,ymin,ymax):
        super().__init__(speed,xmin,xmax,ymin,ymax)
        self.getscreen().tracer(0)
        self.up()
        if 'PurpleAlien.gif' not in self.getscreen().getshapes():   
            self.getscreen().addshape('PurpleAlien.gif')            
        self.shape('PurpleAlien.gif')
        self.goto(random.randint(xmin-1,xmax-1),ymax-20)
        self.setheading(random.randint(250,290))
        self.getscreen().tracer(1)
        Alien.alientList = [x for x in Alien.alienList if x.alive]
        Alien.alienList.append(self)
        self.alive = True
        self.getscreen().ontimer(self.move,200)
                    
    def remove(self):
        self.alive = False
        self.hideturtle()
        
class AlienInvaders:
    def __init__(self,xmin,xmax,ymin,ymax):
        super().__init__()
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def play(self):
        self.mainWin = LaserCannon(self.xmin,self.xmax,self.ymin,self.ymax).getscreen()
        self.mainWin.ontimer(self.addAlien,1000)
        self.mainWin.listen()
        mainloop()

    def addAlien(self):
        if len(Alien.getAliens()) < 7:
            Alien(1,self.xmin,self.xmax,self.ymin,self.ymax)
        self.mainWin.ontimer(self.addAlien,1000)
        
game = AlienInvaders(-200,200,0,400)
game.play()
