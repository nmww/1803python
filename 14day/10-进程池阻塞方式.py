from multiprocessing import Pool
import time
import os
def work():
	for i in range(3):
		time.sleep(1)
		print("哈哈哈哈pid=%d"%os.getpid())

p = Pool(1)

for i in range(10):
	print(i)
	p.apply(work)#阻塞方式

p.close()#关闭池子
p.join()

