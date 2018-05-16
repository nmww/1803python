def w1(fun):
	def inner(*args,**kwargs):
		print("-----验证----")
		print(*args)
		ret =  fun(*args,**kwargs)
		return ret
	return inner


@w1
def test(a,b):
	print("a==%d b==%d"%(a,b))
	return "hehehehe"
@w1
def test():
	print("哈哈哈")

test()
print(test(1,2))
