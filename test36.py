#coding=utf-8

def time_now():
	'''��ʼ�����糿�����ȿ�ʱ��ѽ��'''
	now = raw_input('���ڼ�������')
	
	if now.isdigit() :
		bed_sleep(now)
	else:
		print "��������,����������"
		time_now()

def task_list(tasks):
	'''��Ҫ������ѡ���жϳ�����Ҫ���������б�'''
	print "��������ʲô�أ�"
	
	#num = range(0,len(tasks))
	#��һ��forѭ������ѡ��ǰ�����֣���Ȼ�����0��ʼ��1��ʼ��û��ϵ��
	i = 0
	for t in(tasks):	
		print i,',',t
		i += 1
	
	choice = raw_input('��������ѡ��')
	
	if not choice.isdigit() or int(choice) > len(tasks):
		print "��������ȷ�����֣�"
		task_num(len(tasks))
	elif tasks[int(choice)] == '�����':
		s = 'ϴ��'
		if s in tasks:
			print "�㻹û��%s" % s
			eat_breakfast()	
		else:
			print "�����ؿ�ʼ%s" % tasks[int(choice)]
			del tasks[int(choice)]#���˵�������Զ�ɾ�����ж�Ϊ�����
			task_num(len(tasks))
	elif tasks[int(choice)] == '���ֻ�':
		if not play_phone():
			del tasks[int(choice)]
			task_num(len(tasks))
		else:
			task_list(tasks)
	else:
		print "�����ؿ�ʼ%s " % tasks[int(choice)]
		del tasks[int(choice)]
		task_num(len(tasks))
	
def play_phone():
	'''���ѡ���˿��ֻ�������������жϺ���ѡ��'''
	print "���ֻ������۾��������ȷ����������/��"
	choice = raw_input('>')
	if choice == '��':
		exit("���ǲ���ϧ������")
	elif choice == '��':
		print '�����䰮�۾�'
		return False
	else:
		print "�����룺��/��"
		play_phone()

def eat_breakfast():
	'''�ж�Ҫ��Ҫ����ͣ�ǰ����û��ϴ��'''
	print "������Ҫ��ʼ�������"
	a = raw_input('>')
	if a == '��':
		print 'Ӧ����ϴ��ˢ��������Ŷ'
		exit('��ϰ�߲�Ҫ������')
	elif a == '��':
		print '�������ɺ�ϰ��'
		task_num(len(tasks))
	else:
		print "�����룺��/��"
		eat_breakfast()

def bed_sleep(t):
	'''�����ж��𴲵�ѡ��'''
	print "��Ҫ�𴲻��Ǽ���˯����"
	choice = raw_input(">")
	
	if choice == '˯��':
		if int(t) >= 8:#��Ҫ������ʹ��int����Ȼ�ַ����������жϾ����ֽ���
			exit("������˯����Ҫ�ٵ���������")
		else:
			exit("�Ǿͼ���˯�ɣ���˯��ͷ��")
	elif choice == '��':
		task_list(tasks)
	else:
		print 'û��ã�'
		bed_sleep()
	
def task_num(num):
	'''��������ʣ��������'''
	if num == 0:
		exit('��Ŷ����ʵ���糿������ȥ�ϰ���Ŷ')
	else:
		task_list(tasks)
tasks = ['ϴ��','�����','�����','����','���ֻ�']#�����б���ʵҲ���Ի��ɱ��
time_now()