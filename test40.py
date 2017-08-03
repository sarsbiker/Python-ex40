#coding=utf-8
#下面是关于对象和类的练习
class Song(object):
	
	def __init__(self, lyrics, author):#接受两个参数
		self.lyrics = lyrics#取值方式，定义变量某某等于某某
		self.author = author
		
	def sing_me_a_song(self):#默认每个方法中都需要有self参数
		print '歌手%s曾经唱过这么一首歌：' % self.author 
		for line in self.lyrics:#逐行打印列表内容
			print line
	
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"],'呵呵大')#赋值，要跟类的初始化参数量一致

bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"],'无名')

happy_bday.sing_me_a_song()#调用类中方法时可以留空
happy_bday.name = '没有名字啊'
print happy_bday.name

bulls_on_parade.sing_me_a_song()
