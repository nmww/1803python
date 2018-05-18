from threading import Thread
import time

def sing():
	while True:
		time.sleep(1)
		print("唱歌")


def dance():
	while True:
		time.sleep(1)
		print("跳舞")



t = Thread(target = sing)

t1 = Thread(target = dance)

t.start()
t1.start()

