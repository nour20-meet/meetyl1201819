'''
import turtle
angle = 145
length=120
for i in range(5):
	turtle.forward(length)
	turtle.right(angle)



turtle.mainloop()
'''
'''
import turtle
turtle.begin_fill()
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(45)
turtle.forward(35)
turtle.goto(50,0)
turtle.end_fill()
turtle.mainloop()
''' 
import turtle
turtle.speed(0)
turtle.tracer(3)
for i in range(9000):
	turtle.pendown()
	turtle.forward(200)
	turtle.right(3)
	turtle.forward(100)
	turtle.right(45)
	turtle.forward(50)
	turtle.penup()
	turtle.goto(0,0)
	turtle.right(538)

 	
turtle.mainloop()