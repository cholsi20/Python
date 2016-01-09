class Stock:
	def __init__(self, symbol = " ", name = " ", previousClosingPrice = 1.00, currentPrice = 1.00):
		self.__symbol = symbol
		self.__name = name
		self.__previousClosingPrice = previousClosingPrice
		self.__currentPrice = currentPrice

	#get methods for symbol and name 
	def getSymbol(self):
		return self.__symbol

	def getName(self):
		return self.__name

	#get and set methods for previousClosingPrice and currentPrice
	def getPreviousClosingPrice(self):
		return self.__previousClosingPrice

	def getCurrentPrice(self):
		return self.__currentPrice

	def setPreviousClosingPrice(self, previousClosingPrice):
		self.__previousClosingPrice = previousClosingPrice

	def setCurrentPrice(self, currentPrice):
		self.__currentPrice = currentPrice

	#equation to get percentage of change 
	def getChangePercent(self):
		percentage = (self.__previousClosingPrice - self.__currentPrice) * 100
		return percentage