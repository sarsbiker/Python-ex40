#coding=utf-8
hairs = ['brown','blond','red']
eyes = ['brown','blue','green']
weights = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges','pears','apricots']
change = [1,'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
	print "This is count %d " % number

for fruit in fruits:
	print "A fruit of type: %s" % fruit 

for i in change:
	print "I got %r " % i 

elements = range(0,6)#直接赋值一个列表，或者使用下面的方式
'''
elements = []#定义一个空列表

for i in range(0,6):
	print "Adding %d to the list." % i
	elements.append(i)#在列表末尾加元素
'''
for i in elements:
	print "Element was: %d" % i