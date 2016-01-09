from rectangle_class import Rectangle

#create rectangle with width of 4 and height of 40 
rectangle1 = Rectangle(4, 40)
print("The area of the rectangle with a width of", rectangle1.width, "and a height of", rectangle1.height,
	"is", rectangle1.getArea())
print("The perimeter is", rectangle1.getPerimeter())

#create rectangle with width of 3.5 and height of 35.7 
rectangle1 = Rectangle(3.5, 35.7)
print("The area of the rectangle with a width of", rectangle1.width, "and a height of", rectangle1.height,
	"is", rectangle1.getArea())
print("The perimeter is", rectangle1.getPerimeter())