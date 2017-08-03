#coding=utf-8
'''
def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers =50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20,5+6)

print "And we can aombine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers + 1000)#支持变量和运算

print "测试一下看看"
a=input('第一个数')#raw_input接受都会做字符串处理，input则会区分，字符串加’，数字直接
b=input('第二个数')

cheese_and_crackers(a,b)
'''

def abing(a,b):
	if a > b:
		print '%d 大于 %d ' % (a,b)
	elif a < b:
		print '%d 小于 %d ' % (a,b)
	else:
		print '一样大'

a = input('第一个数')
b = input('第二个数')
#c = input('第三个数')

abing(a,b)
