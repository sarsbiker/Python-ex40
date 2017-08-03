#coding=utf-8
from sys import argv

script,filename = argv 

print "We're going to erase %r." % filename
print "If you don't want that,hit CTRL-C (^C)."
print "If you do want that,hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename,'w')#写模式打开文件，已存在文件会清空，没有就新建，不能使用read()

print "Truncating the file.Goodbye!"
target.truncate()#w模式下不需要

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write(line1+'\n')
#target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally,we close it."
target.close()