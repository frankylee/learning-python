#
#   CS 162P // Instructed by Jim Bailey.
#   Created by frankylee kelly.
#   June 2, 2020
#
# -------------------
#  C A R  C L A S S
# -------------------
# Car Class Requirements
# Your car class should have the following:
#   — initializer that takes a make, color, and year (default: black 1910 Ford)
#   — setters and getters for all three variables
#   — Overloaded equality operator that matches all three variables, return true
#     if they match, false otherwise
#   — Overloaded str() method that returns the contents as (color year make)


class Car:
	"""Car class contains the basic attributes of a car
	attributes: make, color, year
	"""

	def __init__(self, make='Ford', color='Black', year='1910'):
		"""Initializes a car with passed make, model, and year or the
		default values of 'black 1910 Ford'
		"""
		self.make = make
		self.color = color
		self.year = year

	# Getters
	def getMake(self):
		"""Returns the make of a car"""
		return self.make

	def getColor(self):
		"""Returns the color of a car"""
		return self.color

	def getYear(self):
		"""Returns the year of a car"""
		return self.year

	# Setters
	def setMake(self, make):
		"""Update the make of a car"""
		self.make = make

	def setColor(self, color):
		"""Update the color of a car"""
		self.color = color

	def setYear(self, year):
		"""Update the year of a car"""
		self.year = year

	# Overloaded Operators
	def __str__(self):
		"""Defines the string output of a car object"""
		return self.color + " " + str(self.year) + " " + self.make

	def __eq__(self, other):
		"""Defines the equality operator between two car objects; returns boolean"""
		return self.make == other.make and \
		       self.color == other.color and \
		       self.year == other.year

	def __ne__(self, other):
		"""Defines the equality operator between two car objects; returns boolean"""
		return self.make != other.make and \
		       self.color != other.color and \
		       self.year != other.year

