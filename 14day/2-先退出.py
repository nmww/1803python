import os
import time

ret = os.fork()

if ret == 0:
	time.sleep(3)
	print("我是哈哈哈%d"%ret)
else:
	time.sleep(1)
	print("我是呵呵呵%d"%ret)


