import os
import time
rpid = os.fork()

num = 0 

#fork炸弹
#while True:
#	os.fork()

#子进程和父进程的变量每个人都有一份
if rpid == 0:
	num += 1
	time.sleep(5)
	print("我是子进程")
	print("我是子进程的num%d"%num)

else:

	time.sleep(2)
	num -= 1
	print("我是父进程")
	print("父进程的值是%d"%num)
print("我是大王")
