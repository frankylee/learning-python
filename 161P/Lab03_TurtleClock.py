# CS 161P PYTHON
# CREATED BY frankylee kelly.
# LAB 3 — CUSTOM CLOCK FACE TURTLE
#
#
# Write a program to draw the face of a clock
# With user specified:
# 1. background color
# 2. clock/turtle color
# 3. turtle shape
#
# EXTENSIONS //
# 1. Center the clock on the page
# 2. Ask the user how large to make the clock


import turtle

# GET CUSTOM INPUT FROM USER
custom_bg_color = input("What color should the background be? ")
custom_color = input("What color should the clock face be? ")
custom_shape = input("What shape should the face be made of? ")
custom_size = int(input("What size is the clock? "))


# DECLARE THE TURTLE + PROPERTIES
wn = turtle.Screen()
wn.bgcolor(custom_bg_color)

clock = turtle.Turtle()
clock.color(custom_color)
clock.shape(custom_shape)
clock.pensize(3)


# CREATE TURTLE PATH FOR CLOCK FACE
clock.penup()
for i in range(12):
	clock.forward(custom_size)
	clock.pendown()
	clock.forward(10) # DRAWS TICK BEFORE SHAPE
	clock.penup()
	clock.forward(20) # MOVES FROM TICK TO STAMP
	clock.stamp()
	clock.backward(custom_size + 30) # INCREASE SIZE TO ACCOUNT FOR TICK
	clock.left(-30)


# WAIT FOR USER TO CLICK BEFORE EXIT
wn.exitonclick()

