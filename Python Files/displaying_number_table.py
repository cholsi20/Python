#variable declaration
NUMBERS_PER_LINE = 10
counter = 100 #counts in increments to progress loop 
number = 100 

#counter for 200 to 300 
while counter <= 200:
	isDivisible = True #the current number is divisible by 5 and six, but not both 

	#Test if the number is not divisible by 5 and 6, or if it is divisible by both 
	answer = 1
	while answer <= number % 5 :
		if answer <= number % 6:
			#if true, skip this number
			isDivisible = False
			break 
		answer += 1

	#while loop to extract numbers that are both divisible by 5 and 6 and not print them 
	while number % 5 == 0 and number % 6 == 0:
		isDivisible = False
		break

	#if a number is only divisible by 5 or 6, then do this 
	if isDivisible:
		counter += 1

		print(format(number, "2d"), end = ' ')
		if counter % NUMBERS_PER_LINE == 0:
			print() #jump to the next line 

	number += 1


