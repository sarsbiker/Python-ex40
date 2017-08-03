#coding=utf-8
'''
#第一种写法，正题
i = 0
numbers = []

while i < 10:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i +=1
	print "Numbers now:",numbers
	print "At the bottom i is %d" % i

print "The numbers:"

for num in numbers:
	print num
'''
'''
#第二种写法，用函数修改
def num(i,b):
	a = 0
	num = []
	while a < i:
		print "At the top a is %d" % a
		num.append(a)
		a += b
		print "Numbers now:",num 
		print "At the bottom a is %d" % a 
	print "The numbers:"
	for number in num:
		print number

num(input('上限是'),input('间隔多少'))#不能用raw，需要限定为int，否则会死循环。。。
'''
#第三种写法，用for循环和range来代替
def num(a,b):
	for i in range(0,a):
		print "At the top i is %d" % i 
		num = range(0,i+1)
		i +=b 
		print "Numbers now:",num 
		print "At the bottom i is %d" % i 
	for j in range(0,i):
		print j 

num(input('上限值='),input('间隔='))
