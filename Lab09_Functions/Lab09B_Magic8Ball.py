#
#   CS 162P // Instructed by Jim Bailey.
#   Created by frankylee kelly on April 12, 2020.
#   Classroom // Week 1
#
# ---------------------
#   F U N C T I O N S
# ---------------------
#   + MAGIC 8-BALL
# ------------------------
#   Write a function that is called with no parameters and returns a string.
#
#   This function should call the random number generator and get a number between 0 and 19.
#   It will then index into a list of strings and return the appropriate one.
#
#   To model the historic Magic 8 Ball, you can use the list of names found here Wikipedia Magic 8 Ball
#
#   Your main program should initialize the random number generator. Then it should ask the user
#   to enter a question.  if the user replies with the string "Done", then terminate the program.
#   Otherwise, call the function you wrote and output the string it returns.


import random


#   Ask a question to receive your fortune!
#   Keep revealing until user enters DONE.
def main():
	"""Main() creates organization"""
	random.seed()
	seeking = ""

	print("WELCOME TO THE MAGIC 8-BALL!")
	print("Ask a question to reveal your fortune. Enter DONE when finished.")

	while seeking != "done":
		seeking = input("What is that which you seek? ")
		seeking = seeking.lower()

		if seeking != "done":
			print(magic_8ball())
		else:
			print("\nGoodbye!")


#   Returns a random fortune from traditional Magic 8-Ball
#   responses listed in Wikipedia.
def magic_8ball():
	"""This function returns a magic fortune."""
	index = random.randrange(20)
	fortune = [
		"It is certain.",
		"It is decidedly so.",
		"Without a doubt.",
		"Yes - definitely.",
		"You may rely on it.",
		"As I see it, yes.",
		"Most likely.",
		"Outlook good.",
		"Yes.",
		"Signs point to yes.",
		"Reply hazy, try again.",
		"Ask again later.",
		"Better not tell you now.",
		"Cannot predict now.",
		"Concentrate and ask again.",
		"Don't count on it.",
		"My reply is no.",
		"My sources say no.",
		"Outlook not so good.",
		"Very doubtful."
	]
	return fortune[index]


if __name__ == '__main__':
	main()


