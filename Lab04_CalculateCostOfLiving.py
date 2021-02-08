# CS 161P // PYTHON // SUSAN EVANS
# LAB 4 // CREATED BY frankylee kelly.
#
#
# Create a function called over_budget that has five parameters:
# • budget
# • food_bill
# • electricity_bill
# • internet_bill
# • rent
# The function should return True if budget is less than the sum of the other four parameters. Return False otherwise.
#
# Ask the user for their monthly budget, food bill, electric bill, internet bill, and rent. Call the function over_
# budget with those user inputs and tell the user if they were over or under their budget.
#
# Extensions
# 1. If the function returns True, calculate and display how much you were over budget.
# 2. Ask the user for the number of hours worked and hourly wage, use this to calculate the budget. If
# over budget, determine how many more hours you need to work.


# CREATE FUNCTION TO CALCULATE OVER OR UNDER BUDGET
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
	#if budget < food_bill + electricity_bill + internet_bill + rent:
		#return True
	#else:
		#return False

	# SIMPLIFY FUNCTION WITH return bool expression
	return budget < food_bill + electricity_bill + internet_bill + rent


# DEFINE VARIABLES + GET INPUT FROM USER
hours_worked = int(input("How many hours do you work per month? "))
hourly_wage = int(input("What is your hourly wage? "))
groceries = int(input("What is your monthly grocery bill? "))
electricity = int(input("What is your monthly electricity cost? "))
internet = int(input("How much does your internet cost per month? "))
rent = int(input("How much is your rent? "))

budget = hours_worked * hourly_wage
cost_of_living = (groceries + electricity + internet + rent)
debt = cost_of_living - budget
hours_needed = debt / hourly_wage


# DETERMINE OVER OR UNDER BUDGET // CALL FUNCTION // INFORM USER
if over_budget(budget, groceries, electricity, internet, rent):
	print("Your cost of living is", debt, "over budget.")
	print("You need to work", round(hours_needed, 1), "more hours to cover your cost of living.")
else:
	print("Your cost of living is under budget.")

