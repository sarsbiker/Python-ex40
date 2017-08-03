#coding=utf-8
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')#用空格分割字符串转为列表
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#while len(stuff) != 10:
#l = len(stuff)
for l in range(6,10):
	next_one = more_stuff.pop()#取出列表最后的元素
	print "Adding:", next_one
	stuff.append(next_one)#在列表末尾加上前面取出的元素
	print "There are %d items now." % len(stuff)

print "There we go:", stuff

print "Let's do some things with stuff."

print stuff[1]# Oranges
print stuff[-1]# Corn
print stuff.pop()# Corn
print ' '.join(stuff)#用空格将列表重新连接成字符串，相当于split的反转
print '#'.join(stuff[3:5])#stuf[3:5]表示取出第四五个元素，子集了。

