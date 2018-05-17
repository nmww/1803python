import os

rpid = os.fork()

if rpid == 0:
	print("子进程")
else:
	print("父进程")

rpid = os.fork()
if rpid == 0:
	#有可能是子子进程
	#有可能子进程
	print("子进程1")
else:
	#有可能是子进程
	#有可能是父进程
	print("父进程2")

