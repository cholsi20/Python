from StopWatch import StopWatch

def main():
	count = 1000000

	#begin stopwatch module 
	runTime = StopWatch()
	runTime.start()
	endTimeCount = 0
	for number in range(1, count + 1):
		endTimeCount += number 
	#end the stopwatch 
	runTime.stop()

	#display results
	print("The elapsed time it took to count by 1 to 1000000, which began at", runTime.start())
	print("and ended at", runTime.stop())
	print("is", runTime.getElapsedTime(), "milliseconds")

main() #call main 