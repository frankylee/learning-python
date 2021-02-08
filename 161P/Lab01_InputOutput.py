# CS 161P // COMPUTER SCIENCE 1 // PYTHON
# LAB 1 // created by frankylee kelly.

# Write a program that asks the user for their first name,
# last name, and their age. Then your program should output
# the name, current age, and add 10 years to the age.


# Ask the user for their first name, last name, and age
firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
currentAge = input("What is your age? ")

# Increase their age by 10 years
futureAge = int(currentAge) + 10

# Using the details provided, inform the user of a quest
print("If you accept this quest,", firstName, lastName + ',',
      "you will age from", currentAge, "to", futureAge,
      "before you have reached its end.")
