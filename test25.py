#coding=utf-8
def break_words(stuff):
	'''��split�ָ��ַ���'''#�ĵ�ע�⣬shell��ִ��help()���Կ�������
	words = stuff.split(' ')#�ָ��ַ����������ÿո񡢷��ŵ�
	return words

def sort_words(words):
	'''�б�����'''
	return sorted(words)#�ų����¶��С�������sort����������б�
	
def print_first_word(words):
	word = words.pop(0)#pop()�����Ƴ��б��е���� һ��Ĭ�����������һ��
	print word

def print_last_word(words):
	word = words.pop(-1)#�Ƴ������ڶ���
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

