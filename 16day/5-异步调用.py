from multiprocessing import Pool
import time

def test():
	for  i in range(3):
		time.sleep(5)
	
	return "饭好了"

def test2(args):
	print(args)


p  = Pool(3)
p.apply_async(func = test,callback = test2)#非阻塞

while True:
	time.sleep(1)
	print("写作业中")
