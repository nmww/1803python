from threading import Thread
import time

class Test(Thread):
	def run(self):
		while True:
			time.sleep(1)
			print("哈哈哈%s"%self.name)

for i in range(10):
	t = Test()
	t.start()
