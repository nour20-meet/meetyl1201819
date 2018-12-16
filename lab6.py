import turtle
from turtle import Turtle
import random 

# 1
turtle.colormode(255)

class square(Turtle):
	def __init__(self, size ,color):
		Turtle.__init__(self)
		self.shapesize(size)
		self.color(color)
		self.shape("square")
	def random_color(self):
		r=random.randint(0,256)
		b=random.randint(0,256)
		g=random.randint(0,256)
		self.color(r,g,b)

square1 = square(5, "red")
square1.random_color()

# 2

turtle.home()
turtle.pendown()
turtle.begin_poly()
for i in range (6):
	turtle.fd(100)
	turtle.right(60)

turtle.end_poly()	
hexagon = turtle.get_poly()
turtle.register_shape("hexagon", hexagon)


class Hexagon(Turtle):
	def __init__(self, size, color):
		Turtle.__init__(self)
		self.color(color)
		self.shape('hexagon')
		self.shapesize(size)
p = Hexagon(2,'blue')
turtle.mainloop()