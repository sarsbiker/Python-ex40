#coding=utf-8
'''
#��һ��д��������
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
#�ڶ���д�����ú����޸�
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

num(input('������'),input('�������'))#������raw����Ҫ�޶�Ϊint���������ѭ��������
'''
#������д������forѭ����range������
def num(a,b):
	for i in range(0,a):
		print "At the top i is %d" % i 
		num = range(0,i+1)
		i +=b 
		print "Numbers now:",num 
		print "At the bottom i is %d" % i 
	for j in range(0,i):
		print j 

num(input('����ֵ='),input('���='))
