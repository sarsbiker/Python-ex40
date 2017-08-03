#coding=utf-8
'''
def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a + b 

def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a - b 

def multiply(a,b):
	print "MULTIPLYING %d * %d" % (a,b)
	return a * b 

def divide(a,b):
	print "DIVIDING %d / %d" % (a,b)
	return (a+a) / b 

print "Let's do some math with just functions~"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)#赋值，过程中会执行函数中的print

print "Age:%d, Height:%d,Weight:%d,IQ:%d" % (age,height,weight,iq)

print "Here is a puzzle."#趣味题

what = add(age,subtract(height,multiply(weight,divide(iq,2))))
#从最里面的括号开始运行，不打印前面的赋值，直接按新的值运算

print "That becomes:",what,"Can you do it by hand?"
'''
def a(a,b):
	print a
	return a+a*b-1 
	
print a(a(a(input('>'),2),2),2)
