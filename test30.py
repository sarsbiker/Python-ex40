#coding=utf-8
people = 30
cars = 40
trucks = 45
buses = 20

if cars > people and cars > trucks:#如果判断为真就执行
	print 'We should take the cars.'
elif cars < people:#如果上一条为否，就执行这条，这条还是否就继续下面
	print 'We should not take the cars.'
else:#如果上面都没有真的，就只能执行这里咯
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