import os

ret = os.fork()

if ret == 0:
	print("我是哈哈哈%d"%ret)
else:
	print("我是呵呵呵%d"%ret)


