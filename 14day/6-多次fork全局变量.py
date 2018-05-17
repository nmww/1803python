import os

rpid = os.fork()
num = 0

if rpid == 0:
	num += 1
	print("子进程%d"%num)
else:
	num += 2
	print("父进程%d"%num)

rpid = os.fork()
if rpid == 0:
	#有可能是子子进程
	#有可能子进程
	num += 3
	print("子进程1===%d"%num)
else:
	#有可能是子进程
	#有可能是父进程
	num += 4
	print("父进程2===%d"%num)

