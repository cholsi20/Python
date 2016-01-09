#import the Decimal function first 
from decimal import *

#show decimal value of 2.675
exact = Decimal(2.675)

#print the decimal number
print("The decimal value of 2.675 is: ", exact)

#round the decimal value two places 
roundedExact = round(exact, 2)

#print this value
print("If we round this decimal value two places, the number comes to: ", roundedExact)