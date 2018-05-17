from multiprocessing import Process
import time
import os

#这个父进程 在等子进程结束
def test(arg):
	for i in range(5):
		time.sleep(1)
		print("哈哈哈%s pid = %d"%(arg,os.getpid()))

p = Process(target=test,args=("laowang",))
p.start()

#time.sleep(5)

p.join(3) #超时时间
print("hehehehehei")
