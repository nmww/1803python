from threading import Thread,Lock
import time
import threading

g_num = 0
def work():
	global g_num
	for i in range(1000000):
		mutex.acquire()
		g_num+=1
		mutex.release()
	print("%s----%d"%(threading.current_thread().name,g_num))

def work1():
	global g_num
	for i in range(1000000):
		mutex.acquire()
		g_num+=1
		mutex.release()
	print("%s----%d"%(threading.current_thread().name,g_num))

mutex = Lock()

t = Thread(target = work)
t.start()
#t.join()
#time.sleep(2)
t1 = Thread(target = work1)
t1.start()
