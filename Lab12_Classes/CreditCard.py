#
#   CS 162P // Instructed by Jim Bailey.
#   Created by frankylee kelly.
#   May 24, 2020
#
# ----------------------
#  C R E D I T  C A R D
# ----------------------
#   CLASS DESCRIPTION
# ----------------------
# The CreditCard class contains information about a credit account.
#
# The CreditCard class should support the following functions:
#   1. Initialization – the initialization method should take a first and last name, address, card
#      number, and credit limit. The CreditCard initialization will create a Person variable and
#      initialize it with the information passed to CreditCard. If values are not provided when
#      creating a new CreditCard, you should make first name, last name, and address all empty
#      strings. Card number and credit limit should default to 0.
#   2. getBalance – returns the current card balance
#   3. getCardNumber – returns the card number
#   4. getOwnerName – returns the first and last name of the card owner from the associated Person
#   5. getAddress – returns the card holder’s address
#   6. payBalance – this function takes a value as an argument and applies that payment to the
#      balance. Payments must be non-negative values, but a negative balance is acceptable. This
#      function should return a Boolean value: true if the payment was applied and false if it
#      was not (due to negative payment amount).
#   7. makeCharge – this function takes a value and charges that amount to the card, increasing
#      the balance. Charges must be positive and cannot cause the balance to exceed the credit
#      limit. This function should return a Boolean: true if the charge could was applied, false
#      otherwise.
#   8. setCreditLimit – This function takes a value and sets the credit limit to a new value. Note
#      that the credit limit may be set to a value that is below the current balance, but it cannot
#      be set to a negative value.


from Person import Person

class CreditCard:
	"""Contains information on a credit card account
	attributes: number, balance, limit, account
	"""
	account = Person()

	def __init__(self, firstName="", lastName="", address="", number=0, limit=0):
		"""Credit Card initialized by passing account holder, address, and credit account details"""
		self.account = Person(firstName, lastName, address)
		self.number = number
		self.limit = limit
		self.balance = 0

	# Getters
	def getBalance(self):
		"""Returns the current account balance"""
		return self.balance

	def getCardNumber(self):
		"""Returns the credit card number of account"""
		return self.number

	def getOwnerName(self):
		"""Returns the account holder's first and last name"""
		return self.account.firstName + " " + self.account.lastName

	def getAddress(self):
		"""Returns the address on file"""
		return self.account.address

	def getCreditLimit(self):
		"""Returns the account credit limit"""
		return self.limit

	# Setters
	def setCreditLimit(self, value):
		"""Updates the credit limit. Cannot be negative. Returns boolean for new limit set."""
		if value >= 0:
			self.limit = value
			return True
		else:
			return False

	# Methods
	def payBalance(self, payment):
		"""Accepts and applies payment to balance. Returns boolean for valid payment."""
		if payment >= 0:
			self.balance -= payment
			return True
		else:
			return False

	def makeCharge(self, charge):
		"""Accepts and applies charges to balance. Returns boolean for valid charge."""
		if charge >= 0 and charge + self.balance <= self.limit:
			self.balance += charge
			return True
		else:
			return False



