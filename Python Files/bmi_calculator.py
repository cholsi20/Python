#prompt for user weight in pounds
pounds = eval(input("Please enter your weight in pounds: "))

#prompt for user height in inches
inches = eval(input("Please enter your height in inches: "))

# Conversion Equations
weight = (pounds * 0.45359237)

height = (inches * 0.0254)

#BMI Calculation

bmi = weight / ((height) ** 2)

#Output to user
print("Your BMI is ", bmi)