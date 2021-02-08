#
#   CS 162P // Instructed by Jim Bailey.
#   Created by frankylee kelly.
#   April 21, 2020
#
# ---------------------
#  T I C  T A C  T O E
# ---------------------
#   WEEK 3 // LAB 3
# ---------------------
#  PROGRAM DESCRIPTION
# ---------------------
#   For this exercise, you will create a Tic-Tac-Toe game for two players. An optional enhancement
#   would be to create a Computer opponent.
#
#   Program Requirements
#   While this program is an introduction to lists, it will also be a quick review of functions and
#   input validation. Since we have not explicitly covered two dimensional lists, you should use a
#   list of nine elements, one for each space on the board.
#
#   The functions you need to implement are:
#   1) displayInstructions
# 	    a. displays the instructions
# 	    b. does not return anything
#   2) showBoard
# 	    a. pass in board 
# 	    b. display current state 
# 	    c. does not return anything
#   3) getMove
#       a. pass in the board 
#       b. return an updated board 
#       c. must validate move (in range, unoccupied square)
#   4) checkWin
#       a. pass in board
#       b. return true if win
#   5) checkDraw
#       a. pass in board
#       b. return true if draw
#
#   Your program should ask the user if they want to play another game and repeat if the response is y.


# GLOBAL CONSTANTS
X = 'X'
O = 'O'


# Main	Program
def main():
	"""Tic-Tac-Toe"""
	playing = True

	# print instructions first time only
	displayInstructions()

	# game play loop
	while playing:
		win = False
		draw = False

		# initialize board + starting player X
		board = []
		initializeBoard(board)
		player = 0

		# continue playing until win or draw
		while not win and not draw:
			# show board
			showBoard(board)

			# get player's move
			getMove(board, player)

			# check for win
			win = checkWin(board)
			# check for draw
			draw = not win and checkDraw(board)

			# if not win or draw, swap player
			if not win and not draw:
				player = swapPlayer(player)

		# game over message
		if win:
			print("\nPlayer {0} wins!\n".format(X if player == 0 else O))
		if draw:
			print("\nIt's a draw!\n")

		# ask user to play again
		playing = playAgain()


# DISPLAY INSTRUCTIONS
# Print game rules and welcome banner.
def displayInstructions():
	"""Displays game-play instructions"""
	# welcome banner
	print("-----------------------")
	print(" T I C - T A C - T O E ")
	print("-----------------------")
	# game play rules + instructions
	print("Place your mark until the board is full.")
	print("First player to get three across, down, or diagonally wins!")


# INITIALIZE BOARD
# Pass the board at start of game. Set elements to 1-9.
def initializeBoard(board):
	"""Initialize the board at start of game"""
	size = 9
	for i in range(size):
		board.append(i + 1)


# SHOW BOARD
# Print the current board state.
def showBoard(board):
	"""Pass the board to display current state"""
	print("---------------")
	print(" CURRENT BOARD")
	print("---------------")
	print(" " + str(board[0]) + "  |  " + str(board[1]) + "  |  " + str(board[2]))
	print("----+-----+----")
	print(" " + str(board[3]) + "  |  " + str(board[4]) + "  |  " + str(board[5]))
	print("----+-----+----")
	print(" " + str(board[6]) + "  |  " + str(board[7]) + "  |  " + str(board[8]) + "\n")


# GET MOVE
# Pass the board and get player's move.
# Validates input within range and unoccupied move.
# Does not validate alpha-string input.
# Update the board.
def getMove(board, player):
	"""Get player's move and update the board"""
	valid = False
	while not valid:
		move = int(input("Choose your mark: "))
		while move < 1 or move > 9 or board[move - 1] == X or board[move - 1] == O:
			move = int(input("Invalid move! Choose again: "))
		valid = True

	# update the board
	if player == 0:
		board[move - 1] = X
	else:  # player == 1
		board[move - 1] = O


# CHECK WIN -----------------------
# Pass the board and check for win.
def checkWin(board):
	"""Pass the board and check for win"""
	# check rows, columns, diagonal for win
	if (board[0] == board[1] == board[2]) \
			or (board[3] == board[4] == board[5]) \
			or (board[6] == board[7] == board[8]) \
			or (board[0] == board[3] == board[6]) \
			or (board[1] == board[4] == board[7]) \
			or (board[2] == board[5] == board[8]) \
			or (board[0] == board[4] == board[8]) \
			or (board[2] == board[4] == board[6]):
		return True
	return False


# CHECK DRAW ----------------------------
# Pass the board and return true if draw.
def checkDraw(board):
	"""Pass the board and check for draw"""
	for i in range(len(board)):
		if board[i] != X and board[i] != O:
			return False
	return True


# SWAP PLAYER
# Pass current player to return next player.
def swapPlayer(player):
	"""Swap current player"""
	if player == 0:
		player = 1
	else:  # player == 1
		player = 0
	return player


# PLAY AGAIN
# Asks the user to play another round.
def playAgain():
	"""Ask user to play again"""
	valid = False
	# get input from user
	while not valid:
		playing = input("Do you want to play again? Y/N: ")
		playing = playing.upper()
		# validate input
		while playing != 'Y' and playing != 'N':
			playing = input("Invalid response! Y or N: ")
			playing = playing.upper()
		valid = True
	# return response
	if playing == 'Y':
		return True
	return False


if __name__ == '__main__':
	main()
