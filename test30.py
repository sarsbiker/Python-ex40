#coding=utf-8
people = 30
cars = 40
trucks = 45
buses = 20

if cars > people and cars > trucks:#����ж�Ϊ���ִ��
	print 'We should take the cars.'
elif cars < people:#�����һ��Ϊ�񣬾�ִ���������������Ƿ�ͼ�������
	print 'We should not take the cars.'
else:#������涼û����ģ���ֻ��ִ�����￩
	print "We can't decide."

if trucks > cars:
	print "that's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."

if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."