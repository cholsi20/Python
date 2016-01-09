#initial variables 
column = 8 #maximum number of values in a column
maxHeight = column - 1 #creates formatting for each column

#initial for loop to determine initial column height 
for counter in range(column):

    #creates formatting between numbers
    print(maxHeight * "    ", end="")

    #counts maximum height down for each count in initial for loop
    maxHeight -= 1

    #simultaneous assignment for variables in nested for loop 
    number, valueIncrement = 1, counter * 2 + 1

    #nested for lopp to print values
    for secondCounter in range(valueIncrement):
        print("%4d" % number, end="")

        #if else sequence that creates each half of triangle
        if (secondCounter < (valueIncrement // 2)):
            number *= 2
        else:
            number //= 2
    #print new line
    print()