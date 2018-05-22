from socket import *

#创建一个tcp的套接字
s = socket(AF_INET,SOCK_STREAM)

#链接
s.connect(("192.168.1.111",6688))

#链接成功以后发消息

s.send("今晚不见不散".encode("gb2312"))
while True:
	content = s.recv(1024)
	print(content.decode("gb2312"))
s.close()

