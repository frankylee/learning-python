#
#   CS 162P // Instructed by Jim Bailey.
#   Created by frankylee kelly.
#   May 24, 2020
#
# -------------------
#     P E R S O N
# -------------------
#  CLASS DESCRIPTION
# -------------------
# The Person class contains basic biographical information about a person.
#
# The Person class should support the following functions:
#   1. Initializer which accepts a first name, last name, and address
#      (each of which defaults to an empty string)
#   2. get and set function for the first name, last name, and address


class Person:
	"""Basic biographical info about a person
	attributes: firstName, lastName, address
	"""

	# Constructor
	def __init__(self, firstName="", lastName="", address=""):
		"""Person initialized with the passing of first name, last name, and address"""
		self.firstName = firstName
		self.lastName = lastName
		self.address = address

	# Getters
	def getFirstName(self):
		"""Returns the first name of Person"""
		return self.firstName

	def getLastName(self):
		"""Returns the last name of Person"""
		return self.lastName

	def getAddress(self):
		"""Returns the address of Person"""
		return self.address

	# Setters
	def setFirstName(self, name=""):
		"""Change Person's first name"""
		self.firstName = name

	def setLastName(self, name=""):
		"""Change Person's last name"""
		self.lastName = name

	def setAddress(self, newAddress=""):
		"""Update Person's address"""
		self.address = newAddress



