import turtle
import time
import random
from ball import Ball

turtle.tracer(0)
turtle.hideturtle()

running = True
sleep = .0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

my_ball = Ball(0,0,5,5,15,"black")

number_of_balls = 5
minimum_ball_radius = 10
maximum_ball_radius = 100
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5 

balls = []

x = -SCREEN_WIDTH + maximum_ball_radius and SCREEN_WIDTH+ minimum_ball_radius and SCREEN_WIDTH
y = -SCREEN_HEIGHT + maximum_ball_radius and SCREEN_HEIGHT+minimum_ball_radius and SCREEN_HEIGHT