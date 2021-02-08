# CS 161P // PYTHON // SUSAN EVANS
# LAB 8 // GUESS THE WORD
# CREATED BY frankylee kelly.

# GUESS THE WORD //
# Ask the user for 20 words. Create a list containing these words.
#
# Now play Guess the Word:
#   1. Pick a word at random from the list
#   2. Display this word with each letter replaced by an underline.
#   3. Ask the user to guess a letter.
#   4. Display the word with any correctly guessed letters showing and
#      missing letters still represented by underscores.
#   5. Repeat steps 3 and 4 until all letters have been guessed.
#
# EXTENSIONS:
#   1. Show what letters have been guessed
#   2. Keep track of the number of guesses
#   3. Ask if the user wants to play again; if yes, pick another word


import random


# -------------------
#  F U N C T I O N S
# -------------------
# ------------------
#  GET TWENTY WORDS
def get_20_words():
	word_list = []
	for i in range(20):
		word = input("WORD {}: ".format(i + 1))
		word_list.append(word.upper())
	return word_list


# ---------------------------
#  RANDOMIZE INDEX SELECTION
def select_word(alist):
	index = random.randrange(0, 20)
	select = alist[index]
	return select


# ----------------
#   SET THE BOARD
#   This creates the initial board list based on word.
#   Return list to get_guess() to update with each guess
#   example: word = apple; board = [“__“, “__“, “__“, “__“, “__“]
#
def set_board(word):
	board = []

	for i in word:
		board.append("__")

	return board


# -----------------
#   START GUESSING
#   Get guesses from the user until complete.
#   example: word = apple; wordList = [‘a, ‘p’, ‘p’, ‘l’, ‘e’]
#
def get_guess(word):
	boardList = set_board(word)
	wordList= list(word)
	guessed_letters = []  # stores previously guessed
	guessing = True

	# print the display based on boardList
	boardDisplay = " ".join(boardList)
	print(boardDisplay)   # ___ ___ ___ ___ ___
	print()  # spacer

	while guessing:
		# GET GUESS
		guess = input("Guess a letter: ")
		print()  # spacer

		updateBoard = update_board(wordList, boardList, guess.upper())
		boardList = updateBoard[:]

		if guess.upper() not in word:
			guessed_letters.append(guess)
			print("Guessed Letters: ", guessed_letters)
			print()  # spacer

		if boardList == wordList:
			guessing = False


# ----------------
#   UPDATE BOARD
#   Update each guess and print new board.
#   Returns new board to get_guess() to track updates on each pass.
#
def update_board(word, board, guess):
	# setup index increase for multiple letters
	count = word.count(guess)
	incrementIndex = 0

	for i in word:
		index = word.index(i, incrementIndex)
		if i == guess:
			board.pop(index)  # .pop()
			board.insert(index, guess)
		if count > 1:
			incrementIndex += 1

	updateDisplay = " ".join(board)
	print(updateDisplay)   # ___ ___ ___ ___ ___
	print()  # spacer

	return board


# ------------
#   M A I N
# ------------

#   INSTRUCTIONS
print("---------------")
print("GUESS THE WORD")
print("---------------")
print("Enter 20 words to play!")
print()  # spacer

#   GET 20 WORDS
wordBank = get_20_words()

#   SETUP FOR GUESS AGAIN
playing = True

while playing:
	#   CHOOSE WORD
	wordPlay = select_word(wordBank)

	#   PLAY GAME
	get_guess(wordPlay)  # get guess

	#   PLAY AGAIN?
	print("You solved this word!")

	playAgain = input("Would you like to play again? (Y/N): ")
	playAgain = playAgain.upper()

	if playAgain == "Y" or playAgain == "YES":
		playing = True
	else:
		playing = False

