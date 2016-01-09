from stock import Stock 

def main():
	#enter a symbol and name 
	symbol = "INTC"
	name = "Intel Corporation"

	#enter previous and current prices 
	previousClosingPrice = 20.5
	currentPrice = 20.35

	#create stock object
	stock = Stock(symbol, name, previousClosingPrice, currentPrice)

	#display results
	print("The percentage of change for", stock.getSymbol(), stock.getName())
	print("Where the previous day's closing price was", stock.getPreviousClosingPrice())
	print("and the current day's closing price was", stock.getCurrentPrice())
	print("is", format(stock.getChangePercent(), ".2f"), "%")

main() #call the main function