# CS 161P // PYTHON // SUSAN EVANS
# LAB 6 // PIG LATIN
# CREATED BY frankylee kelly.


# PIG LATIN //
# Write a function called createPiggy that takes a word as its parameter and returns another word that represents the
# first word converted to Pig Latin. Remove the first letter of the word, place that letter at the end of the word, and
# then add 'AY'. Create a program that asks the user to input a word and then uses the createPiggy function to
# transform that word to Pig Latin.
#
# The words must be comprised of alphabetic characters only (no numbers or special characters). If a word starts with a
# capital letter, you must make sure the capitalization is transferred to the new word. When the Pig Latin is returned
# to the program it must be displayed in a full sentence with the original word using the .format() method.
# Ex: "Your original word 'Jack' converted to Pig Latin is 'Ackjay'."
#
# EXTENSIONS //
# Create a new unPiggy function to turn a Pig Latin word back to its original version.


# PIG LATIN TRANSLATOR FUNCTION
def createPiggy(string):
	# MAKE PIG LATIN
	# firstChar = string[0]
	# newString = (string[1:] + firstChar + "ay")
	#
	# # MATCH UPPER/LOWER CASE FIRST LETTER
	# if firstChar.isupper():
	# 	newString = newString.capitalize()
	# elif firstChar.islower():
	# 	newString = newString.lower()
	#
	# # MATCH UPPER / LOWER CASE STRING
	# if string.isupper():
	# 	newString = newString.upper()
	# elif string.islower():
	# 	newString = newString.lower()

	# IN CLASS EXAMPLE CODE // MORE EFFICIENT
	if string[0].islower():
		newString = string[1:] + string[0] + "ay"
	else:
		newString = (string[1:] + string[0] + "ay").capitalize()

	return newString


# GET USER INPUT + VALIDATE
while True:
	word = input("Translate a word to Pig Latin:  ")
	if word.isalpha():
		break
	print()  # spacer
	print("Error: Input Invalid. Please enter characters A-Z only.")


# CALL PIG LATIN TRANSLATOR + PRINT
pigLatin = createPiggy(word)
print()  # spacer
print("The word '{}' translated in Pig Latin is '{}'.".format(word, pigLatin))

