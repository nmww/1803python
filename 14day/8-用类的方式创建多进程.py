from multiprocessing import Process
import time


class Dog(Process):
	
	def __init__(self):
		Process.__init__(self)
		self.name = "a"
		

	#一定重写run方法
	def run(self):
		for i in range(5):
			time.sleep(1)
			print("process dog")



dog = Dog()
dog.start()
dog.join()
