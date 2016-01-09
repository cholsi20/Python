#import random
import random 

# genrate a random number that is less than 100 for the first integer
number1 = random.randrange(0,100)

#generate a random number that is less than 100 for second integer 
number2 = random.randrange(0,100)

#evaluate total for these integers when added 
total = number1 + number2

#prompt user to enter their answer for the sum of these two numbers 
userAnswer = eval(input("Please enter the sum of " + str(number1) + " + " + str(number2) + ": "))

#create condition that evaluates their answer as either true or false 
if userAnswer == total:
	print(bool(1))

else: 
	print(bool(0))