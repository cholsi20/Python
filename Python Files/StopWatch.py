import time

class StopWatch:
	def __init__(self):
		self.__startTime = time.time()

	#get methods for start and end 
	def getStartTime(self):
		return self.__startTime

	def getEndTime(self):
		return self.__endTime 

	#define start and stop 
	def start(self):
		self.__startTime = time.time()

	def stop(self):
		self.__endTime = time.time()

	#getting elapsed time 
	def getElapsedTime(self):
		elapsedTime = (self.__endTime - self.__startTime) * 1000
		return elapsedTime