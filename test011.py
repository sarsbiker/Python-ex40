#coding=utf-8
'''
print "你年纪多大啦",
print "你多高？",
'''
age = input("你年纪多大啦")

height = raw_input('身高多少厘米呢')
print "你体重多少呢？",
weight = raw_input()

print "所以你%r 岁，身高%s 厘米 ，体重%r 公斤。" % (
	age,height,weight)
	