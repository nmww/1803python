from threading import Thread
import time

def work():
	time.sleep(1)
	print("i love you")

for i in range(5):
	t = Thread(target=work)
	t.start()

