import os
import time

#父进程返回的ret是就是子进程的pid
#子进程的ppid就是父进程的pid
ret = os.fork()

if ret == 0:
	print("我是子进程%d pid=%d ppid=%d"%(ret,os.getpid(),os.getppid()))
else:
	print("我是父进程%d pid=%d ppid=%d"%(ret,os.getpid(),os.getppid()))


