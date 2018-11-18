import turtle
from turtle import Turtle
import random 
turtle.colormode(255)

class square(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)
	def rand_color(self):
		r=random.randint(0,256)
		b=random.randint(0,256)
		g=random.randint(0,256)
		self.color(r,g,b)

x=square(9)
x.rand_color()	

turtle.mainloop()	

