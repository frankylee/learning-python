#
#   CS 162P // Instructed by Jim Bailey.
#   Created by frankylee kelly.
#   May 6, 2020
#
# -------------------------------
#  D U N G E O N  C R A W L  2.0
# -------------------------------
#   WEEK 5 // LAB 5
# ---------------------
#  PROGRAM DESCRIPTION
# ---------------------
#   For more practice with functions and validation, we will be doing a second version of the Dungeon
#   Crawl game. You may still add monsters moving randomly if you would like.
# ------------------------
#   Program Requirements
#   You need to implement the following features. I realize that this might cause you to have to change
#   some of your design features, but this is to give you the specific practice that I am looking for. You
#   should validate that all numbers are positive integers on input and trap any attempt to enter a nonnumeric value.
# ------------------------
#   constant.py
#       this is a separate module used for declaring constants.
#       These include default parameter values, object symbols, etc.
#   displayInstructions()
#       this function will display the instructions for playing this game
#   userDefinedSize()
#       this function should return true if the user wants to define the dungeon size
#   getSize()
#       return a tuple for the user requested dungeon size
#   createMap(width, height)
#       this function will create the 2D list for the map and return it to main after it has been created.
#       This can be called with default values for the default size, or with custom values from getSize
#   validYesNo()
#       should be used any place the user is required to select yes or no
#       should return true for yes and false for no.
#   placeTrap(map, numTraps)
#       The place functions should be called from within createMap
#   placeTreasure(map, numTreasure)
#       and should take the map and number of each thing being
#   placePlayer(map)
#       placed into the map and place the appropriate number of objects randomly into the map. Default parameters
#       should be defined in constant.py and specified in function definition
#   findEmpty(map)
#       this method will be used in createMap. When called, it will find a random location on the map that is
#       empty and return a tuple (row, column) for that location
#   findPlayer(map)
#       this function will find the player location on the map and return a tuple (row, column) of where it is
#   getMove(map)
#       this function should get a move from the player and return a tuple containing the new location of the player.
#       This function should only return a move after validating that it is within the array. The player should also
#       be allowed to choose the letter q to quit the game and return (-1, -1) to main
#   checkQuit(move)
#       if the player has chosen to quit the game, this should be used to terminate the game loop
#       without the use of break
#   checkBounds(map, move)
#       this function should be called inside of getMove and validate whether or not the player has attempted to
#       move outside of the bounds of the list.
#   checkWin(map, move)
#       these functions should accept the map and move and test
#   checkLose(map, move)
#       whether the chosen move will cause the player to win or lose the game. Should return true or false.
#       Should not update the map. The result of these should be used to terminate the game loop without
#       the use of break
#   updateMap(map, move)
#       this function should accept the map and move from main and use them to update the Map. You should not
#       update the map unless not win and not lose.
#   playAgain()
#       after the game is over, this function should see if the player wishes to start again. Should return true
#       or false. Should use validYesNo. If the user wants to play again, start over with a new dungeon


import constant
import random


def main():
	"""Dungeon Crawl 2.0"""
	random.seed()  # initialize starting seed
	playing = True

	# display instructions
	displayInstructions()

	# outer game loop
	while playing:
		quit_game = False
		win = False
		lose = False

		# ask to define dungeon size and initialize
		if userDefinedSize():
			size = getSize()
			dungeon = createMap(size[0], size[1])
		else:
			dungeon = createMap()

		# game loop
		while not quit_game and not win and not lose:
			# display the dungeon
			displayDungeon(dungeon)

			# get move from player
			move = getMove(dungeon)

			# check for quit
			quit_game = checkQuit(move)
			# win if treasure is found
			win = not quit_game and checkWinLose(dungeon, constant.TREASURE, move)
			# if treasure not found, look for trap
			lose = not quit_game and not win and checkWinLose(dungeon, constant.TRAP, move)

			# if not win or lose, update dungeon for next move
			if not quit_game and not win and not lose:
				updateDungeon(dungeon, move)

		# game over message
		if win:
			print("\n\"You find the treasure and escape the dungeon!\"\n")
		elif lose:
			print("\n\"You fall into a trap and perish!\"\n")
		elif quit_game:
			print("\n\"You chose to quit this round!\"\n")

		# ask user to play again
		playing = playAgain()


# ------------------------
#   DISPLAY INSTRUCTIONS
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


# ---------------------
#   USER DEFINED SIZE
#   This function should return true if the user wants to define the dungeon size.
def userDefinedSize():
	"""Does user want to define the dungeon size? Returns bool."""

	# get input from user
	answer = validYesNo("Do you want to define the size of the dungeon? (Y/N): ")
	print()  # spacer after input

	return answer


# ------------
#   GET SIZE
#   Return a tuple for the user requested dungeon size.
def getSize():
	"""Get dungeon dimensions from user. Returns tuple."""

	# instructions to the user
	print("Dimensions must be at least 4x4, but no bigger than 20x20.")

	# get number from user using getNum()
	width = getNum("Enter the width: ", 4, 20)
	height = getNum("Enter the height: ", 4, 20)

	print()  # spacer after input

	return width, height


# --------------
#   CREATE MAP
#   This function will create the 2D list for the map and return it to main after it has been created.
#   This can be called with default values for the default size, or with custom values from getSize.
#   Randomly places traps, treasure, and the player.
def createMap(width=constant.SIZE, height=constant.SIZE):
	"""Creates 2D list map and returns to main."""

	dungeon = []
	# initialize 2D list to empty spaces
	for row in range(height):
		dungeon.append([])
		for col in range(width):
			dungeon[row].append(constant.SPACE)

	# modify numTraps based on size of map
	num_traps = width * height // 5

	# randomly place traps
	boardPlacement(dungeon, constant.TRAP, num_traps)

	# randomly place treasure
	boardPlacement(dungeon, constant.TREASURE)

	# randomly place player
	boardPlacement(dungeon, constant.PLAYER)

	return dungeon


# ------------------------------
#   placeTrap(map, numTraps)
#   placeTreasure(map, numTreasure)
#   placePlayer(map)
#       The place functions should be called from within createMap and should take the map and number of each
#       thing being placed into the map and place the appropriate number of objects randomly into the map.
#       Default parameters should be defined in constant.py and specified in function definition
# -------------------
#   BOARD PLACEMENT
#   Helper function randomly places passed object in the dungeon.
def boardPlacement(dungeon, map_object, count=constant.ONE):
	"""Randomly place objects in dungeon at start of game."""

	# place as many map_objects as needed
	for i in range(count):
		# find empty coordinates
		coordinates = findEmpty(dungeon)

		# extract row and col from coordinate tuple
		row = coordinates[0]
		col = coordinates[1]

		# place the object
		dungeon[row][col] = map_object


# --------------
#   FIND EMPTY
#   This method will be used in boardPlacement. When called, it will find a random location on the map that is
#   empty and return a tuple (row, column) for that location.
def findEmpty(dungeon):
	"""Find empty coordinates on map and return as tuple."""

	# modify dimensions based on variable size
	width = len(dungeon[0])
	height = len(dungeon)

	empty = False

	# search until found
	while not empty:
		#  generate coordinates
		row = random.randrange(height)
		col = random.randrange(width)

		# if coordinates empty, return to boardPlacement()
		if dungeon[row][col] == constant.SPACE:
			empty = True

	return row, col


# -------------------
#   DISPLAY DUNGEON
#   Pass the map to display.
def displayDungeon(dungeon):
	"""Display the dungeon"""

	height = len(dungeon)

	# print on single line without brackets
	for i in range(height):
		print("  " + "  ".join(dungeon[i]))
	print()  # spacing after dungeon


# ---------------
#   FIND PLAYER
#   Helper function finds player's current coordinates.
#   Returns x, y as tuple.
def findPlayer(dungeon):
	"""Locate player and return coordinates as tuple"""

	# modify dimensions based on variable size
	width = len(dungeon[0])
	height = len(dungeon)

	# find player within dungeon
	for i in range(height):
		for j in range(width):
			if dungeon[i][j] == constant.PLAYER:
				return i, j


# ----------------
#   getMove(map)
#       This function should get a move from the player and return a tuple containing the new location of the player.
#       This function should only return a move after validating that it is within the array. The player should also
#       be allowed to choose the letter q to quit the game and return (-1, -1) to main
# ------------
#   GET MOVE
#   Gets and validates a move (L, R, U, D) from player.
#   Pass player's current location and return the move.
def getMove(dungeon):
	"""Get move from user & validate input"""

	valid = False

	while not valid:
		try:
			move = input("Which direction do you move?: ")
			move = move[0].upper()

			# validate player input
			while (move != constant.U and move != constant.D and move != constant.L
		           and move != constant.R and move != constant.Q):
				move = input("You can only enter U, D, L, R, or Q: ")
				move = move[0].upper()

			valid = checkBounds(dungeon, move)

			# return player's new location
			movePlayer = updateXY(move, findPlayer(dungeon))

		except:
			print("Error! Please enter a valid move.")

	return movePlayer


# ---------------
#   CHECK BOUNDS
#   This function should be called inside of getMove() and validates whether or not the player has
#   attempted to move outside of the bounds of the list.
def checkBounds(dungeon, move):
	"""Validates player's move within bounds of dungeon."""

	# modify bounds based on variable size
	xBound = len(dungeon[0]) - 1
	yBound = len(dungeon) - 1

	# find player's location
	location = findPlayer(dungeon)
	# update coordinates based on move
	coordinates = updateXY(move, location)
	x = coordinates[0]
	y = coordinates[1]

	# check for quit
	if move == constant.Q:
		return True
	# if not quit, check for out of bounds
	elif x < 0 or x > xBound or y < 0 or y > yBound:
		print("\nYou cannot escape the dungeon!\n")
		return False
	# if not quit and in bounds, move valid
	return True

# --------------
#   CHECK QUIT
#   If the player has chosen to quit the game, this should be used to terminate
#   the game loop without the use of break.
def checkQuit(move):
	"""Checks for request to quit game. Returns bool."""

	# check if player selected quit
	if move == constant.QUIT:
		return True
	return False

# -----------------------
#   checkWin(map, move)
#   checkLose(map, move)
#       These functions should accept the map and move and test whether the chosen move will cause the player
#       to win or lose the game. Should return true or false. Should not update the map. The result of these
#       should be used to terminate the game loop without the use of break.
# --------------------
#   CHECK WIN / LOSE
#   Pass the dungeon, the object code (trap or treasure), and move.
#   Check if move is on trap or treasure. Return bool.
def checkWinLose(dungeon, objectCode, move):
	"""Check move for trap or treasure. Returns bool."""

	x = move[0]
	y = move[1]

	# did player find trap or treasure?
	if dungeon[x][y] == objectCode:
		return True
	return False

# ------------------
#   UPDATE DUNGEON
#   Pass the dungeon and move from main() to update map for the next turn.
def updateDungeon(dungeon, move):
	"""Update the dungeon map for the next round."""

	# find player's previous location; reset to space
	location = findPlayer(dungeon)
	x = location[0]
	y = location[1]
	dungeon[x][y] = constant.SPACE

	# update coordinates based on move
	x = move[0]
	y = move[1]
	dungeon[x][y] = constant.PLAYER

# --------------
#   PLAY AGAIN
#   Ask the user if they want to play again.
#   Use validYesNo() helper function.
def playAgain():
	"""Ask user to play another game of Dungeon Crawl."""

	# get input from user
	playing = validYesNo("Do you want to play again? Y/N: ")

	return playing

# -------------------------
#   UPDATE XY COORDINATES
#   Helper function updates the x and coordinates based on move.
def updateXY(move, coordinates):
	"""Updates player's coordinates based on move."""

	x = coordinates[0]
	y = coordinates[1]

	# update based on player's move
	if move == constant.U:
		x -= 1
	elif move == constant.D:
		x += 1
	elif move == constant.L:
		y -= 1
	elif move == constant.R:
		y += 1
	elif move == constant.Q:
		return constant.QUIT

	return x, y

# ---------------------
#   VALIDATE YES / NO
#   Use any place the user is required to select yes or no.
#   Return true for yes and false for no.
def validYesNo(instruction):
	"""Helper function validates Y/N input. Returns bool."""

	valid = False
	# get Y or N from user
	while not valid:
		try:
			# get input from user
			user_input = input(instruction)
			user_input = user_input.upper()
			# validate
			if user_input[0] != 'Y' and user_input[0] != 'N':
				print("Please enter Y or N.")
			else:
				valid = True
		except:
			print("Error! Enter Y or N.")

	return user_input[0] == 'Y'

# --------------
#   GET NUMBER
#   Helper function gets a number within range from the user.
def getNum(instruction, min, max):
	"""Pass the range and get a valid number from user."""

	valid = False
	# get number from user
	while not valid:
		try:
			num = int(input(instruction))
			if num < min or num > max:
				print("Invalid! Enter number between {0} and {1}.".format(min, max))
			else:
				print()  # spacer after valid input
				valid = True
		except:
			print("Error! Enter a number.")

	return num

if __name__ == '__main__':
	main()
