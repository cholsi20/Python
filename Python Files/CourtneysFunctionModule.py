# courtney's first function module! 
import random

def printMatrix(n):
	#counter for number of rows to print 
	for counter in range(0, n):
		#counter for number of random integers to print 
		for counter in range(1, n + 1):
			#prints a random 0 or 1 horizontally 
			print(random.randint(0,1), end =' ')
			#prints a row that is only n values long
			if counter % n == 0:
				print()


def format(number, width):
	count = 0 
	for char in number:
		count = count + 1

	#prints message for user 
	print("The formatted number is: ")

	#subtract count from width entered
	zeros = width - count 

	#determines if there should be zeros in front of number 
	if zeros > 0:
		for counter in range(0, zeros):
			print(0, end='')

	print(number)
	print()


def reverse(number):
	#create a string to store characters in the stack
	reverse = ""
	#count through characters 
	for counter in number:
		#counter adds each character to to the stack to create reverse of original character array 
		reverse = counter + reverse
	#return the fully reversed array
	return(reverse)


def printChars(ch1, ch2, numberPerLine):
	#convert characters to integers 
	character1 = ord(ch1)
	character2 = ord(ch2)

	#define a counter to use to create orrect line breaks that are not subject to whatever character range 
	lineBreak = 0
	#count each number in the range, adding a one to second character to insure that number is inclusive
	for counter in range(character1, character2 + 1):
		#print the character values of each integer 
		print(chr(counter), end =' ')
		lineBreak = lineBreak + 1
		#create line breaks! 
		if lineBreak % numberPerLine == 0:
			print()
	print()



	