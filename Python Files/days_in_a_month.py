# import math functions 
import math

# introduce user to program
print("How many days were there the month you were born, or the month your sibling was born?\
  How about your mother?  You can use this program to find out!  ")

# prompt user to enter month and year 
month = eval(input("Please input the month as a number: "))
year = eval(input("Please enter a year: "))

leapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
	

if True:
	#determines month to calculate days correctly 
	if month == 2:
		numberOfDays = 29 + ((month + math.floor(month/8)) % 2) + (2 % month + (2 * math.floor(1/month)))
	else:
		numberOfDays = 28 + ((month + math.floor(month/8)) % 2) + (2 % month + (2 * math.floor(1/month)))

# for not a leap year
else:
	numberOfDays = 28 + ((month + math.floor(month/8)) % 2) + (2 % month + (2 * math.floor(1/month)))


#change month to print a string and print results 
if month == 1:
	print("January ", year, " has ", numberOfDays, " number of days.")
elif month == 2:
	print("February ", year, " has ", numberOfDays, " number of days.")
elif month == 3:
	print("March ", year, " has ", numberOfDays, " number of days.")
elif month == 4:
	print("April ", year, " has ", numberOfDays, " number of days.")
elif month == 5:
	print("May ", year, " has ", numberOfDays, " number of days.")
elif month == 6:
	print("June ", year, " has ", numberOfDays, " number of days.")
elif month == 7:
	print("July ", year, " has ", numberOfDays, " number of days.")
elif month == 8:
	print("August ", year, " has ", numberOfDays, " number of days.")
elif month == 9:
	print("September ", year, " has ", numberOfDays, " number of days.")
elif month == 10:
	print("October ", year, " has ", numberOfDays, " number of days.")
elif month == 11:
	print("November ", year, " has ", numberOfDays, " number of days.")
else:
	print("December ", year, " has ", numberOfDays, " number of days.")




