#coding=utf-8
print "����������ϰ��ϰ"
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
print "This should be five:%s" % five #%s������S
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans,jars,crates

start_point = 10000
beans,jars,crates = secret_formula(start_point)#ͬʱ����������

print "With a starting point of: %d" % start_point
print "We'd have %d beans,%d jars,and %d crates." % (beans,jars,crates)

start_point /= 10#��д��a=a/10  a/=10

print "We can also do that this way:"
print "We'd have %d beans,%d jars, and %d crates." % secret_formula(start_point)#ֱ���ú���ʽ�ķ���ֵ����ַ��������ñ���