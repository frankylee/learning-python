#
#   CS 162P // Instructed by Jim Bailey.
#   Created by frankylee kelly on April 12, 2020.
#   Classroom // Week 2
#
# ---------------------
#   R E C U R S I O N
# ---------------------
#   + BEST PRACTICES
# ---------------------
#   WHAT IS RECURSION?
#   Recursion is an algorithmic approach where a program calls itself to solve some problem. It has
#   the advantage of often simplifying the algorithm, but at the cost of added memory and runtime.
#
#   There are three requirements of any recursive program:
#       1) It has a base case that causes it to terminate
#       2) It calls itself
#       3) When	it calls itself, the arguments move toward the base case.
#
# ---------------------
#   PRACTICE PROBLEMS
# ---------------------
#   STRING REVERSER
#   This function reads a string and returns it in reverse order. The only string methods you should
#   use are removing the first character and appending a char to a string.
# ---------------------
#   EXPONENT
#   Write a recursive function that takes two arguments, base and exponent. It then multiplies the
#   base times itself exponent times using recursion.
# ---------------------
#   PALINDROME DETECTOR
#   A palindrome is a string that reads the same forward and backward. Write a recursive function that
#   takes a string and returns true if it is a palindrome. The algorithm is to compare the first and
#   last letters, if they match, keep going with the inner string. If they do not match, return false.
#   If the string is empty or one character, return true.
# ---------------------
#   SUBSTRINGS
#   This is a more complex problem, you are to take a string and return all substrings of it.
#   For example:
#       A -> A
#       AB -> AB, A, B
#       ABC -> ABC, AB, AC, BC, B, C
# ---------------------


def main():
	"""Recursive Function Practice"""
	print(string_reverser("We're all mad here."))
	print(exponent(4, 2))           # 16
	print(power_rec(3, 3))          # 27
	print(palindrome("weather"))    # false
	print(palindrome("tacocat"))    # true
	print(substringOf("NOPE"))


def string_reverser(string):
	"""Reads a string and returns the reverse order"""
	# base case (return when length is 1 char)
	if len(string) == 1:
		return string
	# call on all but first letter; append first letter to the end
	return string_reverser(string[1:]) + string[0]


def exponent(base, exp):
	"""Recursively executes base to the exponential power"""
	if exp <= 0:    # base case of 0
		return 1
	# call itself, reduce exp, and multiply
	return base * exponent(base, exp - 1)


def power_rec(base, exponent):
	# base case
	if exponent == 1:
		result = base
	# move toward base of 1
	else:
		result = base * power_rec(base, exponent - 1)
	# recursively call
	return result  # base * power_rec(base, exponent - 1)


def palindrome(string):
	"""Read a string and detect palindrome"""
	# base case, string of 1 or empty
	if len(string) <= 1:
		return True
	if string[0] != string[-1]:
		return False
	return palindrome(string[1:-1])


def substringOf(string):
	"""Takes a string and outputs all substrings of it"""
	temp = [string]

	# add all substrings starting with first value
	# add all substrings starting without first value
	if len(string) > 0:
		temp.extend(substringOf(string[1:]))
		temp.extend(substringOf(string[:-1]))

	# use set to remove duplicates
	return list(set(temp))


if __name__ == '__main__':
	main()




