# CIS 007 Introduction to Python Programming 
# Courtney Holsinger 
# June 12, 2015
import turtle

#initial set up 
turtle.penup()
turtle.goto(0,0)
turtle.left(90)
turtle.pendown()

#top right square
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

#bottom left square
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

# left bottom square
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

#left top square
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

# finishing position
turtle.right(90)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
