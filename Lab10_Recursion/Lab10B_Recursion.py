#
#   CS 162P // Instructed by Jim Bailey.
#   Created by frankylee kelly.
#   April 13, 2020
#
# ---------------------
#   R E C U R S I O N
# ---------------------
#   WEEK 2 // LAB 2
# ---------------------
#   Write a recursive function with two parameters, base and power, both are integers (but you do not need
#   to verify this). Your function is to return base raised to power, but by using the following algorithm.
#
#   Consider the following:                      FIND THE PATTERN
#       X^15 is X * (X^14)                odd = base * (base, exp - 1)
#       X^14 is (X^7) * (X^7)            even = (base, exp / 2) * (base, exp / 2)
#       X^7 is X * (X^6)
#       X^6 is (X^3) * (X^3)
#       X^3 is X * (X^2)
#       X^2 is X * X
#       X is X
#
#   Note that if we do this as a recursive function, we have 7 function calls instead of the 15 it would take
#   if we just did the multiplication. Look at this example and see if you can recognize the pattern and see
#   how it treats odd exponents differently than even exponents. Once you see this, you should be able to code
#   your recursive function.
#
#   For this lab, any exponent less than 0 should return 1 as its default behavior.
#
# ----------------------------------
#       A   |   B   |   RETURN
#    ----------------------------
#       5       1         5
#       2      13        8192
#       3       6        729
#       5       8       390625
#       27      0         1
#       13     -1         1
# ----------------------------------


def main():
	print(power(5, 1))      # 5
	print(power(2, 13))     # 8192
	print(power(3, 6))      # 729
	print(power(5, 8))      # 390625
	print(power(27, 0))     # 1
	print(power(13, -1))    # 1


#   recursive power function
def power(base, exp):
	"""Takes two integers and returns the power of base to the exponent."""
	# default behavior
	if exp <= 0:
		return 1
	# base case
	elif exp == 1:
		return base
	# bring each call closer to base
	elif exp % 2 == 0:  # exp is even
		return power(base, exp / 2) * power(base, exp / 2)
	# if exp is not even, then it's odd
	return base * power(base, exp - 1)


if __name__ == '__main__':
	main()


