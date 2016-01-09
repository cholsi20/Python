# prompt user for first integer
number1 = eval(input("Please enter your first of three integers: "))

# prompt user ofr sencond integer
number2 = eval(input("Please enter the second integer: "))

# prompt for third integer
number3 = eval(input("Please enter the third and final integer: "))

#the folloing determined the ordering of these integers
if number1 < number2:
	number1, number2 = number2, number1
	if number1 < number3:
		number1, number3 = number3, number1
	if number2 < number3:
		number2, number3 = number3, number2


elif number1 < number3:
	number1, number3 = number3, number1
	if number1 < number2:
		number1, number2 = number2, number1
	if number2 < number3:
		number2, number3 = number3, number2
			

else:
	print("From greatest to least the order of your integers is: ", number1, number2,number3)


#prints max to min 
print("From greatest to least the order of your integers is: ", number1, number2,number3)