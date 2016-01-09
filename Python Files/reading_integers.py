#introduces program
print("Hello!  To begin, simply enter an integer.\nEnter 0 at any time to end the program.")
print()

#prompts user for integer
number = eval(input("Please enter an integer: "))

#determines if 0 right away
if number == 0:
	print("You did not enter a number")

total = 0 #decalres variable for sum 
averageCounter = 0 #counts how many numbers in the set
while number != 0:
	total += number #adds each integer to create sum of all integers user enters 
	averageCounter += 1


	positive = 0 # declares variable for positive integers 
	negative = 0 # declares variable for negative integers 

	if number % 2 == 0:
		positive += 1 
	else:
		negative += 1

	number = eval(input("Please enter an integer: "))

# equation to determine average 
average = total / averageCounter 

#prints output 
print("The number of positive integers is: ", positive)
print("The number of negative integers is: ", negative)
print("The sum of all the integers entered is: ", total)
print("The average of all the integers is: ", average)

