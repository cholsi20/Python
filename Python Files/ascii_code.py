#prompts user for ASCII code, or integer between 0 and 127
n = eval(input("Enter an ASCII code by entering an iteger between 0 and 127: "))

#evaluate string as ASCII
x = chr(n)

#print the character represented by that code
print("The number ", n, " is the ASCII code for ", x)