#coding=utf-8
#�����ǹ��ڶ���������ϰ
class Song(object):
	
	def __init__(self, lyrics, author):#������������
		self.lyrics = lyrics#ȡֵ��ʽ���������ĳĳ����ĳĳ
		self.author = author
		
	def sing_me_a_song(self):#Ĭ��ÿ�������ж���Ҫ��self����
		print '����%s����������ôһ�׸裺' % self.author 
		for line in self.lyrics:#���д�ӡ�б�����
			print line
	
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"],'�ǺǴ�')#��ֵ��Ҫ����ĳ�ʼ��������һ��

bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"],'����')

happy_bday.sing_me_a_song()#�������з���ʱ��������
happy_bday.name = 'û�����ְ�'
print happy_bday.name

bulls_on_parade.sing_me_a_song()
