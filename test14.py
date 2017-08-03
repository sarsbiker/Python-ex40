#coding=utf-8
from sys import argv

script,user_name,companny = argv 
p = '>>>'

print "Hi %s,I'm the %s script." % (user_name,script)
print "I'd like to ask you a few questions."
print "Do you in companny %s?" % companny
likes = raw_input(p)

print "Where do you live %s?" % user_name
lives = raw_input(p)

print "What kind of computer do you have?"
computer = raw_input(p)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer.Nice.
""" % (likes,lives,computer)