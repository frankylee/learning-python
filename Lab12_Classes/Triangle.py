#
#   CS 162P // Instructed by Jim Bailey.
#   Created by frankylee kelly.
#   May 14, 2020
#
# -------------------
#  T R I A N G L E
# -------------------
#  CLASS DESCRIPTION
# -------------------
#  Define a class to implement a Triangle:
#  • Each Triangle is defined by the length of its 3 sides. Each length is an integer. You can name
#    the sides whatever you want, but you do need three variables in your class.
#  • The initializer function for your Triangle class should create a triangle with sides of 3, 4, and
#    5 when called with no parameters. If it is called with three parameters, it should save those as
#    the sides of the triangle. You can call the three sides anything you want internally in your code.
#  • The Triangle class should have three methods that allow setting of the sides. These should
#    be called setA, setB, and setC. They each will have a single parameter that is saved as one
#    of the three sides. You do not need to verify that they are called with integers, but you
#    should save the values as integers in your class.
#  • The Triangle class should have three methods that allow getting of the sides. These should be
#    called getA, getB, and getC. They have no parameters and just return the appropriate side values.
#  • The Triangle class should have four additional methods isEquilateral(), isScalene(), isIsosceles(),
#    and isRight(). Each of these has no input parameters and returns a boolean value that is true if
#    the appropriate condition is met, false otherwise.
#      • isEquilateral – all three sides are equal
#      • isIsosceles -- at least two sides are equal (either just 2 or all 3)
#      • isScalene – no two sides are equal
#      • isRight – the square of one of the sides is equal to the sum of the squares of the other
#        two sides (You should check all three combinations)


class Triangle:
	"""A simple class to create and evaluate triangles.

	attributes: a, b, c,
	"""

	# Triangle Initializer
	def __init__(self, a=3, b=4, c=5):
		"""Triangle constructor. Default values: 3, 4, 5"""
		self.a = int(a)
		self.b = int(b)
		self.c = int(c)

	# String output
	def __str__(self):
		"""Overrides default string output for a triangle object. Displays each side's length."""
		return "Triangle's sides: a = {}, b = {}, c = {}".format(self.a, self.b, self.c)

	# Getters
	def getA(self):
		"""Returns side A of triangle"""
		return self.a

	def getB(self):
		"""Returns side B of triangle"""
		return self.b

	def getC(self):
		"""Returns side C of triangle"""
		return self.c

	# Setters
	def setA(self, a):
		"""Defines side A of triangle"""
		self.a = int(a)

	def setB(self, b):
		"""Defines side B of triangle"""
		self.b = int(b)

	def setC(self, c):
		"""Defines side C of triangle"""
		self.c = int(c)

	# Methods
	def isEquilateral(self):
		"""Returns true if all three sides are equal"""
		return self.a == self.b == self.c

	def isIsosceles(self):
		"""Returns true if at least 2 sides are equal"""
		return self.a == self.b or self.a == self.c or self.b == self.c

	def isScalene(self):
		"""Returns true if no two sides are equal"""
		return self.a != self.b != self.c

	def isRight(self):
		"""Returns true if the square of one side is equal to the sum of the squares of the other two sides"""
		if self.sq(self.a) == self.sq(self.b) + self.sq(self.c):
			return True
		elif self.sq(self.b) == self.sq(self.a) + self.sq(self.c):
			return True
		elif self.sq(self.c) == self.sq(self.a) + self.sq(self.b):
			return True
		return False

	# Helper method
	def sq(self, x):
		"""Returns the square of x"""
		return x * x
