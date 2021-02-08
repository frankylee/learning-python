# CS 161P // PYTHON // SUSAN EVANS
# LAB 5 // CREATED BY frankylee kelly.
#
# Write a program that allows the user to play a guess my number game:
# • The computer should generate a random number between 1 and 100.
# • The user will then enter a number and the computer will respond with:
# “Too high” or “Too low” or You got it”.
# • If the user did not guess the correct number, the computer should continue to loop getting another guess.
# • If the user guessed correctly, the computer should report how many guesses it took and terminate.
#
# You will need to use at least one function in the program, it is up to you which piece of code is
# best suited to a function.
#
# EXTENSIONS
# 1. Validate the input to be between 1 and 100.
# 2. Ask the user if they want to play again and restart the game if they do.
# 3. Output a list of previously guessed numbers before each new guess.


import random


# VALIDATE INPUT FUNCTION
def validate(number):
	while number < 1 or number > 100:
		number = int(input("Error: Guess a number 1 to 100: "))

	if 1 <= number <= 100:
		prevNums.add(number)


# GUESS AGAIN FUNCTION
def guessAgain(guess, luckyNum):
	attempts = 1

	if guess == luckyNum:
		print("You got it!")
		return attempts
		
	while guess != luckyNum:
		# TOO HIGH, TOO LOW, YOU GOT IT
		if guess < luckyNum:
			print("Too low!")
		else:
			print("Too high!")

		print()  # spacer
		print("Guessed Numbers:", prevNums)

		guess = int(input("Guess again: "))
		validate(guess)

		attempts += 1

	return attempts


# INTRO + INSTRUCTIONS
print("GUESS MY NUMBER ::")

# VARIABLES
playing = True
prevNums = set()


while playing:
	# GENERATE NUMBER 1-100
	luckyNum = random.randrange(1, 101)

	# GET GUESS FROM USER
	guess = int(input("Guess a number between 1 and 100: "))
	validate(guess)

	# KEEP GETTING GUESSES
	attempts = guessAgain(guess, luckyNum)
	print()  # spacer
	print("It took", attempts, "tries to get it right!")

	# PLAY AGAIN
	print()  # spacer
	playAgain = input("Would you like to play again? (Y/N): ")
	playAgain = playAgain.lower()
	if playAgain == 'y' or playAgain == 'yes':
		playing = True
		prevNums.clear()
	else:
		playing = False
	print()  # spacer

# end while playing

