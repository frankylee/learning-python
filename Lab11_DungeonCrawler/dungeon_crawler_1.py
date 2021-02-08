#
#   CS 162P // Instructed by Jim Bailey.
#   Created by frankylee kelly.
#   April 28, 2020
#
# --------------------------
#  D U N G E O N  C R A W L
# --------------------------
#   WEEK 4 // LAB 4
# ---------------------
#  PROGRAM DESCRIPTION
# ---------------------
#   While the program is an introduction to two-dimensional lists, it is also a review of functions and
#   input validation.
#
#   Create a program that displays a simple dungeon and allows the player to explore it. For example, in
#   the following example G is the player, T is a trap, and X is the treasure. If you hit a trap, you fail.
#   If you reach the treasure you win.
#
#   Each turn, the player will input a character for Left, Right, Up, or Down and move the player accordingly.
#   Define the size of your dungeon with a constant MAX_SIZE using a constants.py module. Create the dungeon
#   as 2D list that is MAX_SIZE * MAX_SIZE.
#
#   You will need to create and use the following functions:
#       1) createDungeon – initializes a dungeon
#           a) Input – the dungeon and an integer count
#           b) Function – randomly places count traps in the dungeon and one treasure and the player
#       2) displayDungeon – displays a dungeon
#           a) Input – the dungeon
#           b) Function – display the dungeon
#           c) Return – nothing
#       3) getMove – gets and validates a move (L, R, U, D)
#           a) Input – current location
#           b) Function – input a move code and validate it (valid code, move inside dungeon)
#           c) Return – the move code or a new location
#       4) checkMove – sees if the move is onto a trap or treasure
#           a) Input – the dungeon, object code you are checking for (trap or treasure), move code
#           b) Function – check the move to see if onto a space containing the object code
#           c) Return – true if moved onto such a space
#           d) This function checks both for traps and finding treasure.
#       5) updateDungeon -- updates the dungeon for the next cycle
#           a) Input – the dungeon and move code
#           b) Function – update the dungeon moving the player marker
# ----------------
#   Enhancements
#   For a more advanced version, add several monsters that randomly move one step in any direction each term.
#   They must not go outside the limits of the dungeon. If the player moves onto an occupied square, she loses.
#   Your program could also ask the user if they want to play another game and repeat with a new dungeon if
#   the response is yes.


import random
import constant


def main():
	"""Dungeon Crawler"""
	random.seed()  # initialize starting seed
	playing = True

	# display instructions
	displayInstructions()

	# outer game loop
	while playing:
		# variables
		win = False
		lose = False
		dungeon = []
		traps = 16

		# initialize dungeon
		dungeon = createDungeon(dungeon, traps)

		# game loop
		while not win and not lose:
			# display the dungeon
			displayDungeon(dungeon)

			# get move from player
			move = getMove(dungeon)

			# win if treasure is found
			win = checkMove(dungeon, constant.TREASURE, move)
			# if treasure not found, look for trap
			lose = not win and checkMove(dungeon, constant.TRAP, move)

			# if not win or lose, update dungeon for next move
			if not win and not lose:
				updateDungeon(dungeon, move)

		# game over message
		if win:
			print("\n\"You find the treasure and escape the dungeon!\"\n")
		else:
			print("\n\"You fall into a trap and perish!\"\n")

		# ask user to play again
		playing = playAgain()


# DISPLAY INSTRUCTIONS
def displayInstructions():
	"""Prints game play instructions and welcome banner"""
	print("---------------------------")
	print(" D U N G E O N   C R A W L ")
	print("---------------------------")
	print("Explore the dungeon looking for treasure——but be sure to avoid the traps!")
	print("If you hit a trap, you lose. If you reach the treasure, you win.\n")
	print("    LEGEND       VALID MOVES")
	print("  Player: @          Up: U")
	print("    Trap: #        Down: D")
	print("Treasure: X        Left: L")
	print("                  Right: R")
	print("-----------------------------\n")


# CREATE DUNGEON
# Pass the dungeon and number of traps to initialize.
# Randomly places traps, treasure, and the player.
def createDungeon(dungeon, traps):
	"""Initialize the dungeon"""
	# initialize array to spaces
	dungeon = [[constant.SPACE for i in range(constant.SIZE)] for j in range(constant.SIZE)]

	# randomly place traps
	for i in range(traps):
		boardPlacement(dungeon, constant.TRAP)

	# place the treasure
	boardPlacement(dungeon, constant.TREASURE)

	# place the player
	boardPlacement(dungeon, constant.PLAYER)

	return dungeon


# DISPLAY DUNGEON
# Pass the dungeon to display
def displayDungeon(dungeon):
	"""Display the dungeon"""
	# print on single line without brackets
	for i in range(constant.SIZE):
		print("  " + "  ".join(dungeon[i]))
	print()  # spacing


# GET MOVE
# Gets and validates a move (L, R, U, D) from player.
# Pass player's current location and return the move.
def getMove(dungeon):
	"""Get move from user & validate input"""
	valid = False

	while not valid:
		move = input("Which direction do you move?: ")
		move = move.upper()

		# validate player input
		while move[0] != constant.U and move[0] != constant.D and move[0] != constant.L and move[0] != constant.R:
			move = input("You can only move U, D, L, R: ")
			move = move.upper()

		# locate player's coordinates
		location = locatePlayer(dungeon)
		# update coordinates based on move
		coordinates = updateXY(dungeon, move, location)
		x = coordinates[0]
		y = coordinates[1]
		# check move within dungeon walls
		if x < 0 or x > 8 or y < 0 or y > 8:
			print("\nYou cannot escape the dungeon!\n")
		else:
			valid = True
	return move


# CHECK MOVE
# Check if move is on trap or treasure.
# Pass the dungeon, the object code (trap or treasure), and move.
def checkMove(dungeon, objectCode, move):
	"""Check move for trap or treasure"""
	# locate player's coordinates
	location = locatePlayer(dungeon)
	# update coordinates based on move
	coordinates = updateXY(dungeon, move, location)
	x = coordinates[0]
	y = coordinates[1]

	if dungeon[x][y] == objectCode:
		return True
	return False


# UPDATE DUNGEON
# Pass the dungeon and move code to update for next turn.
def updateDungeon(dungeon, move):
	"""Update the dungeon for next move"""
	# locate player's coordinates
	location = locatePlayer(dungeon)
	x = location[0]
	y = location[1]
	dungeon[x][y] = constant.SPACE

	# update coordinates based on move
	coordinates = updateXY(dungeon, move, location)
	x = coordinates[0]
	y = coordinates[1]
	dungeon[x][y] = constant.PLAYER


# PLAY AGAIN
# Ask the user to play again.
def playAgain():
	"""Ask user to play Dungeon Crawler"""
	valid = False
	# get input from user
	while not valid:
		playing = input("Do you want to play again? Y/N: ")
		playing = playing.upper()
		# validate input
		while playing[0] != 'Y' and playing[0] != 'N':
			playing = input("Please enter Y or N: ")
			playing = playing.upper()
		valid = True
	return playing[0] == 'Y'


# BOARD PLACEMENT
# Helper function randomly places passed object in the dungeon.
def boardPlacement(dungeon, object):
	"""Pass element to randomly place in dungeon"""
	hidden = False

	while not hidden:
		#  generate coordinates
		row = random.randrange(constant.SIZE)
		col = random.randrange(constant.SIZE)

		# if coordinates empty, place object
		if dungeon[row][col] == constant.SPACE:
			dungeon[row][col] = object
			hidden = True


# LOCATE PLAYER
# Helper function finds player's current coordinates.
def locatePlayer(dungeon):
	"""Locate player and return coordinates as tuple"""
	for i in range(constant.SIZE):
		for j in range(constant.SIZE):
			if dungeon[i][j] == constant.PLAYER:
				return [i, j]


# UPDATE XY COORDINATES
# Helper function updates the x and coordinates based on move.
def updateXY(dungeon, move, coordinates):
	# update based on player's move
	if move == constant.U:
		coordinates[0] -= 1
	elif move == constant.D:
		coordinates[0] += 1
	elif move == constant.L:
		coordinates[1] -= 1
	elif move == constant.R:
		coordinates[1] += 1
	return coordinates


if __name__ == "__main__":
	main()
