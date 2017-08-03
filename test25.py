#coding=utf-8
def break_words(stuff):
	'''用split分割字符串'''#文档注解，shell中执行help()可以看到内容
	words = stuff.split(' ')#分割字符串，可以用空格、符号等
	return words

def sort_words(words):
	'''列表排序'''
	return sorted(words)#排除，新队列。区别于sort是针对已有列表
	
def print_first_word(words):
	word = words.pop(0)#pop()用于移除列表中的最后 一个默认留空是最后一个
	print word

def print_last_word(words):
	word = words.pop(-1)#移除倒数第二个
	print word

def sort_sentence(sentence):
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

