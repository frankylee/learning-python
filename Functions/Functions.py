#
#   CS 162P // Instructed by Jim Bailey.
#   Created by frankylee kelly on April 6, 2020.
#
# ---------------------
#   F U N C T I O N S
# ---------------------
#   LAB 1 // WEEK ONE
# ---------------------
#   Write a function with two parameters, a and b. It returns true if a is a power of b.
#   You are to use the following algorithm: a is a power of b, if a is divisible by b and a/b is divisible by b.
#   Remember to check for the two default cases (a is a power of a and 1 is a power of a).
#
#   REQUIRED TESTS // Check function with the following values:
#       A   |   B   |   RETURN
#   ----------------------------
#        5      5       True
#       25      5       True
#      125     25       False
#        1     13       True
#       64      4       True
#       27      4       False
#      256      2       True
#   -----------------------------
#   — if a is 1 and b is 0, result is true because 0^0 = 1
#   — if a is 0 result is false because 0 cannot be a power of non-zero
#   — if b is 0 result is true only if a is 1, otherwise false
# -------------------------------


def main():
	"""Main Function creates organization."""
	print("  5 power of  5: " + str(isPower(5, 5)))     # True
	print(" 25 power of  5: " + str(isPower(25, 5)))    # True
	print("125 power of 25: " + str(isPower(125, 25)))  # False
	print("  1 power of 13: " + str(isPower(1, 13)))    # True
	print(" 64 power of  4: " + str(isPower(64, 4)))    # True
	print(" 27 power of  4: " + str(isPower(27, 4)))    # False
	print("256 power of  2: " + str(isPower(256, 2)))   # True


def isPower(a, b):
	"""Return True if a is power of b"""
	# catch base cases before attempt to divide by 0
	# 0^0 = 1
	if a == 1 and b == 0:
		return True
	# zero cannot be power of non-zero
	# non-zero cannot be power of zero
	elif a == 0 or b == 0:
		return False
	# if a == b (b ^ 1) // if a == 1 (b ^ 0)
	elif a == b or a == 1 or (a % b == 0 and (a/b) % b == 0):
		return True
	else:
		return False


if __name__ == '__main__':
	main()

	# ---------
	#  TESTING
	# print("\n\n" + "---- TESTING ----")
	# print("       a == 0: " + str(isPower(0, 4)))       # False
	# print("       b == 0: " + str(isPower(120, 0)))     # False
	# print("       a == b: " + str(isPower(30, 30)))     # True
	# print("a == 1, b == 0 " + str(isPower(1, 0)))       # True


