#prompt user for two integers
n1 = eval(input("Enter the first integer: "))
n2 = eval(input("Enter the second integer: "))

#determine which vale is greatest, and use simultateous assignment to achieve an initial value for d 
if n2 > n1:
	n1,n2 = n2, n1

#set initial looping values for GCD and variable n
d = n2
gcd = 1


#begin while loop to count variable gcd up by one, until it reaches the greatest divisor value using counter n
while d <= n1 and d <= n2:
	if n1 % d == 0 and n2 % d == 0:
		gcd = d
		break

	d -= 1


#print the final output of the loop
print("The greatest common divisor of ", n1, " and ", n2, " is ", gcd)