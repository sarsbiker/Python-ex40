#coding=utf-8
print "来来来，练习练习"
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love 
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print "----------------"
print poem
print "----------------"

five = 10 - 2 + 3 - 6
print "This should be five:%s" % five #%s不能用S
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans,jars,crates

start_point = 10000
beans,jars,crates = secret_formula(start_point)#同时定义多个变量

print "With a starting point of: %d" % start_point
print "We'd have %d beans,%d jars,and %d crates." % (beans,jars,crates)

start_point /= 10#简写，a=a/10  a/=10

print "We can also do that this way:"
print "We'd have %d beans,%d jars, and %d crates." % secret_formula(start_point)#直接用函数式的返回值插进字符串，不用变量