#coding=utf-8
def print_two(*args):
	arg1,arg2 ,arg3= args #复杂一点的方式，类似之前使用argv
	print "arg1:%r,arg2:%r,arg3:%s" % (arg1,arg2,arg3)
	
def print_two_again(arg1,arg2):
	print "arg1:%r, arg2:%r" % (arg1,arg2)

def print_one(arg1):
	print "arg1:%r" % arg1

def print_none():#用：来表示这一行结束
	print "I got nothing."#四个空格或者直接TAB就行
#函数末尾要空行，结束
print_two("A","B",'我')
print_two_again("X","Y")
print_one("SSSSS")
print_none()