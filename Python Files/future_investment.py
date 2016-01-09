#asks user for investment amount
initialInvestmentAmount = eval(input("Please enter your initial investment amount: "))

#asks user for annual interest rate 
interestRate = eval(input("Please enter the interest rate for your investment: "))

#asks user for number of years investing
yearsInvesting = eval(input("Please enter over how many years you are investing: "))

#math to determine the future investment value
futureInvestmentValue = initialInvestmentAmount * ((1 + (interestRate / 1200)) ** (yearsInvesting * 12))

#print out of future investment value
print("Your accumulated value is $", futureInvestmentValue)