#coding=utf-8
from sys import argv

script,input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0) #seek起始位置为文件中的第几个字符

def print_a_line(line_count,f):
	print line_count,f.readline()#读取一行

current_file = open(input_file)

print "first let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line,current_file)
#rewind(current_file) #说明当前读取的位置在文件的哪里
#current_line += 1#是下面那种的简写，+=更快
print_a_line(current_line,current_file)#每次运行readline后，都会读完一行，然后继续运行就是下一行
print current_line
current_line = current_line + 1
print_a_line(current_line,current_file)

current_file.close()