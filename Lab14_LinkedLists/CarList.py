#
#   CS 162P // Instructed by Jim Bailey.
#   Created by frankylee kelly.
#   June 2, 2020
#
# ------------------
#   C A R  L I S T
# ------------------
# List Class Requirements
# Your list class should have the following:
#   — a link class that contains a pointer to next and a reference to a car object
#   — addCar – input is make, color, year. Creates a new car, creates a new link that
#     points to that car and adds it to the head of the list
#   — findCar – input is make, color, year. Creates a temporary car with those inputs.
#     Uses the overloaded equality operator to check the list to see if such a car
#     exists. Returns true if found, false otherwise
#   — removeHead – if list is empty, returns none. Otherwise returns the car at the
#     head of the list and removes it from the list
#   — Overloaded str() method that uses the car str() method to create a string of
#     all the cars in the list. The cars should be listed one per line.
#   — Overloaded len() method that returns the number of cars in the list


from Car import Car


class Link:
	"""Basic link structure for CarList"""

	def __init__(self, car=Car()):
		"""Links hold a car object and pointer to the next object in list"""
		self.car = car
		self.next = None


class CarList:
	"""A linked list of car objects with functionality to add, remove,
	get number of items, and search from list
	"""

	def __init__(self):
		"""Creates a new link in the list."""
		self.head = None

	def addCar(self, make, color, year):
		"""Creates a new car link and adds it to the head of the list"""
		self.newLink = Link(Car(make, color, year))
		self.newLink.next = self.head
		self.head = self.newLink

	def removeHead(self):
		"""Returns the car at the head of the list and removes it (or None)"""
		if self.head is None:
			return None
		self.temp = self.head
		self.head = self.temp.next
		return self.temp.car

	def findCar(self, make, color, year):
		"""Creates a temporary car with passed input and uses the overloaded
		equality operator to search the list. Returns boolean for found"""
		self.search = Link(Car(make, color, year))
		self.current = self.head
		while self.current is not None:
			if self.current.car == self.search.car:
				return True
			self.current = self.current.next
		return False

	# Overloaded Operators
	def __str__(self):
		"""Defines the string output of a list of cars. Works with the car str()
		method to create a string of all the cars in the list one per line."""
		self.output = ""
		self.current = self.head
		while self.current is not None:
			self.output += str(self.current.car) + "\n"
			self.current = self.current.next
		return self.output

	def __len__(self):
		"""Returns the number of cars in the list"""
		self.count = 0
		self.current = self.head
		while self.current is not None:
			self.count += 1
			self.current = self.current.next
		return self.count

