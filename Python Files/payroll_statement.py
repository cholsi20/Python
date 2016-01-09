# reads employee name
name = input("Please enter your name: ")

# asks for number of hours worked
hoursWorked = eval(input("Please enter the number of hours worked for one week: "))

# asks for hourly pay rate
payRate = eval(input("Please enter your hourly pay rate: "))

# math to calculate gross pay
gross = hoursWorked * payRate

# calculation to determine federal withholding at 20%
federalWithholding = gross * (0.20)

# calculation for state withholding at 9.0%
stateWithholding = gross * (0.09)

# calculation for total deductions
totalDeductions = federalWithholding + stateWithholding

# calculation for net pay
netPay = gross - totalDeductions

# formatted printout for this information to the console 
print("Employee Name: ", name)
print("Hours worked per week: ", hoursWorked)
print("Hourly pay rate: ", payRate)
print("Gross pay: ", format(gross, ".2f"))

print("Deductions: ")
print("\t Federal Withhoding at 20.0%\ is: ", format(federalWithholding, ".2f"))
print("\t State Withhoding at 9.0%\ is: ", format(stateWithholding, ".2f"))
print("\t Employee total deductions are: ", format(totalDeductions, ".2f"))

print("Net Pay is: ", format(netPay, ".2f"))