#prompts user for integer input
number = eval(input("Please submit any integer between 0 and 1000: "))

#variable assignment for addition 
x = number % 10

y = number // 10

z = y % 10

a = y // 10 

final = x + z + a

#output to user with sum 
print("The sum of the digits in ", number, " is ", final)