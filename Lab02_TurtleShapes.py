# CS 161P // COMPUTER SCIENCE 1 // PYTHON
# LAB 2 // created by frankylee kelly.

# Write a program that draws a polygon. You must ask the user for the number of sides
# (between 3 to 20), and for a length (between 20 and 100).
# Your program must also ask the user for the background color, pen color,
# pen width, and fill color for your polygon.


# ASK USER FOR DETAILS ON THEIR CUSTOM SHAPE
sides = int(input("For your custom shape, pick a number of sides between 3-20: "))
length = int(input("Choose a number between 20-100 for length: "))
bgcolor = input("Pick a background color for the artboard: ")
pencolor = input("What color is your pen? ")
pensize = int(input("What is your pen's width? "))
fillcolor = input("Pick a fill color for your shape: ")


# CREATE CUSTOM TURTLE BASED ON USER INPUT
import turtle
wn = turtle.Screen()
wn.bgcolor(bgcolor)

custom = turtle.Turtle()
custom.color(pencolor)
custom.pensize(pensize)
custom.fillcolor(fillcolor)

custom.begin_fill() # BEGINS FILL SHAPE

for i in range(sides):
	custom.forward(length)
	custom.left(360 / sides)

custom.end_fill() # ENDS FILL SHAPE


# CREATE HEXAGONAL TURTLE
hex = turtle.Turtle()
hex.pensize(2)

# CENTER TURTLE
hex.up()
hex.goto(-60, -60)
hex.down()

for i in range(6):
	hex.color("dark slate blue")
	hex.forward(90)
	hex.left(60)


# CREATE CENTERED OCTAGONAL TURTLE
oct = turtle.Turtle()
oct.pensize(3)

# CENTER TURTLE
oct.up()
oct.goto(-60, -90)
oct.down()

for i in range(8):
	oct.color("lavender")
	oct.forward(90)
	oct.left(45)


# WAIT FOR USER TO CLICK ON CANVAS BEFORE CLOSING
wn.exitonclick()


# NOTE
# This program does not have validation for user input.
