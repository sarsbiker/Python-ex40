#coding=utf-8
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')#�ÿո�ָ��ַ���תΪ�б�
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#while len(stuff) != 10:
#l = len(stuff)
for l in range(6,10):
	next_one = more_stuff.pop()#ȡ���б�����Ԫ��
	print "Adding:", next_one
	stuff.append(next_one)#���б�ĩβ����ǰ��ȡ����Ԫ��
	print "There are %d items now." % len(stuff)

print "There we go:", stuff

print "Let's do some things with stuff."

print stuff[1]# Oranges
print stuff[-1]# Corn
print stuff.pop()# Corn
print ' '.join(stuff)#�ÿո��б��������ӳ��ַ������൱��split�ķ�ת
print '#'.join(stuff[3:5])#stuf[3:5]��ʾȡ���������Ԫ�أ��Ӽ��ˡ�

