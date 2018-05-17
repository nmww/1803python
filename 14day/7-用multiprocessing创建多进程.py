from multiprocessing import Process
import time
import os

#这个父进程 在等子进程结束
def test(arg):
	for i in range(5):
		time.sleep(1)
		print("老大%s pid = %d"%(arg,os.getpid()))

def test1(arg):
	for i in range(5):
		time.sleep(1)
		print("老二%s pid = %d"%(arg,os.getpid()))

p = Process(target=test,args=("laowang",))
p.start()


p1 = Process(target=test1,args=("xiaowang",))
p1.start()
#time.sleep(5)

p.join() #超时时间
p1.join()
print("hehehehehei")
