#begin rectangle definition 

class Rectangle:
	#construct rectangle object
	def __init__(self, width = 1, height = 2):
		self.width = width
		self.height = height

	#def __init__(self, height = 2):
		

	#get equations to compute values for variables of class Rectangle
	def getPerimeter(self):
		return (2 * self.width) + (2 * self.height)

	def getArea(self):
		return self.width * self.height

	def setWidthHeight(self, width, height):
		self.width = width
		self.height = height

	#def setHeight(self, height):
		