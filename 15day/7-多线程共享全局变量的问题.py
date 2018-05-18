from threading import Thread
import time
import threading

g_num = 0

flag = 1
def work():
	global g_num
	global flag
	if flag == 1:
		for i in range(1000000):
			g_num+=1
		print("%s----%d"%(threading.current_thread().name,g_num))
		flag =2

def work1():
	global g_num
	global flag
	while True:
		if flag == 2:
			for i in range(1000000):
				g_num+=1
			print("%s----%d"%(threading.current_thread().name,g_num))
			break

t = Thread(target = work)
t.start()
#t.join()
#time.sleep(2)
t1 = Thread(target = work1)
t1.start()
