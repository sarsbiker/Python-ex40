#coding=utf-8
#from sys import argv
#from os.path import exists

#script,from_file,to_file = argv
#open(to_file,'w').write(open(from_file).read())
open('test17_3.txt','w').write(open('test17_1.txt').read())
#print "Copying from %s to %s" % (from_file,to_file)

#in_file = open(from_file)
#indata = in_file.read()

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#exists用于判断文件是否存在，存在为True
#print "Ready,hit RETURN to conitune,CTRL-C to abort."
#raw_input()

#out_file = open(to_file,'w')
#out_file.write(open(from_file).read())

#print "Alright,all done."
#out_file.close() 
#in_file.close()