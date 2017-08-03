#coding=utf-8

def time_now():
	'''起始程序，早晨醒来先看时间呀！'''
	now = raw_input('现在几点啦？')
	
	if now.isdigit() :
		bed_sleep(now)
	else:
		print "输入有误,请输入数字"
		time_now()

def task_list(tasks):
	'''主要的任务选择判断程序，需要输入任务列表'''
	print "接下来做什么呢？"
	
	#num = range(0,len(tasks))
	#用一个for循环来列选项前的数字，当然这个从0开始和1开始都没关系咯
	i = 0
	for t in(tasks):	
		print i,',',t
		i += 1
	
	choice = raw_input('输入数字选择：')
	
	if not choice.isdigit() or int(choice) > len(tasks):
		print "请输入正确的数字："
		task_num(len(tasks))
	elif tasks[int(choice)] == '吃早餐':
		s = '洗漱'
		if s in tasks:
			print "你还没有%s" % s
			eat_breakfast()	
		else:
			print "你愉快地开始%s" % tasks[int(choice)]
			del tasks[int(choice)]#做了的任务就自动删除，判断为已完成
			task_num(len(tasks))
	elif tasks[int(choice)] == '看手机':
		if not play_phone():
			del tasks[int(choice)]
			task_num(len(tasks))
		else:
			task_list(tasks)
	else:
		print "你愉快地开始%s " % tasks[int(choice)]
		del tasks[int(choice)]
		task_num(len(tasks))
	
def play_phone():
	'''如果选择了看手机就运行这个，判断后续选择'''
	print "看手机会让眼睛不舒服，确认吗，输入是/否"
	choice = raw_input('>')
	if choice == '是':
		exit("真是不爱惜健康！")
	elif choice == '否':
		print '不错，珍爱眼睛'
		return False
	else:
		print "请输入：是/否"
		play_phone()

def eat_breakfast():
	'''判断要不要吃早餐，前提是没有洗漱'''
	print "你现在要开始吃早餐吗？"
	a = raw_input('>')
	if a == '是':
		print '应该先洗漱刷牙后吃早餐哦'
		exit('坏习惯不要继续啦')
	elif a == '否':
		print '不错，养成好习惯'
		task_num(len(tasks))
	else:
		print "请输入：是/否"
		eat_breakfast()

def bed_sleep(t):
	'''用来判断起床的选择'''
	print "你要起床还是继续睡觉？"
	choice = raw_input(">")
	
	if choice == '睡觉':
		if int(t) >= 8:#不要忘记了使用int，不然字符串跟数字判断就是字节了
			exit("不能再睡啦，要迟到啦！！！")
		else:
			exit("那就继续睡吧，别睡过头哈")
	elif choice == '起床':
		task_list(tasks)
	else:
		print '没想好？'
		bed_sleep()
	
def task_num(num):
	'''用来计算剩余任务数'''
	if num == 0:
		exit('哇哦，充实的早晨，可以去上班了哦')
	else:
		task_list(tasks)
tasks = ['洗漱','吃早餐','做早操','看书','看手机']#任务列表，其实也可以换成别的
time_now()