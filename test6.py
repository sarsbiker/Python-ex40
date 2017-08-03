#coding=utf-8
x = '这里有%d类人。' % 10
binary = 'binary'
do_not = 'don\'t'
y = '有些知道%s 还有些%s' % (binary,do_not)

#打印一下看看
print x 
print y 

print 'i said:%s' % x 
print 'i also said:"%s"' % y 

hilarious = False
joke_evaluation = "isn't that joke so funny? %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e 