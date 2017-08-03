#coding=utf-8
from sys import argv

script,filename = argv #命令行写入赋值

txt = open(filename) #读取某个文件并赋给变量

print "Here's your file %r:" % filename
print txt.read() #读变量的内容

#print "Type the filename again:"
#file_again = raw_input(">")

#txt_again = open(file_again)

print txt_again.read()
