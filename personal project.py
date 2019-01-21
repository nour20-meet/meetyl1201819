from turtle import *
import turtle 
import random
import math
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.shape("circle") 
		self.shapesize(r/10) 
		self.r = r
		self.color(color)
		self.penup()
		self.dx = dx
		self.dy = dy 
		self.goto(x,y)
	def move (self, screen_widht, screen_height):	
		oldx = self.xcor()
		oldy = self.ycor()
		new  = oldx + self.dx
		new  = oldy + self.dy
		right_side = newx + self.radius
		left_side = newx - self.radius
		top_side = newy + self.radius
		bottom_side = newy - self.radius

		self.goto(newx, newy)
		if top_side > screen_height or bottom_side < screen_height:
			self.dx *= -1
		if top_side < screen_widht or bottom_side > screen_widht:
			self.dy *= -1

			
ball1 = Ball(0,0,20,20,40,"pink")