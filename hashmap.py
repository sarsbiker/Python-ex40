#coding=utf-8
def new(num_buckets=1):#给参数赋予默认值，如果调用的时候没有填值就会使用默认的
	aMap = []
	for i in range(0,num_buckets):
		aMap.append([])#列表末尾增加空列。运行之后是[[],[]]
	return aMap

def hash_key(aMap, key):
	return hash(key) % len(aMap)# %表示求余数，恰好是倍数的话就会得0
	#hash() 用于获取取一个对象（字符串或者数值等）的哈希值。返回的就是 一段编码，比如数字，唯一

def get_bucket(aMap, key):
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]#取出列表里的对应的元素，依然是列表。这是二维的多行多列表

def get_slot(aMap, key, default=None):
	bucket = get_bucket(aMap, key)#根据对应的键或者说字段某一行，取对应值，也就是选出某一列
	
	for i,kv in enumerate(bucket):#遍历已有列表中结果，对比是否已存在
		#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
		k, v = kv#键值匹配
		if key == k:#如果输入的键已经存在
			return i, k, v #返回索引数字，键，值
			#谨防输入联想错误
	return -1, key, default#返回结果为空

def get(aMap, key, default=None):
	i, k, v = get_slot(aMap, key, default=default)
	return v #根据输入的键获取对应的值，只返回值

def set(aMap, key, value):
	bucket = get_bucket(aMap, key)#
	i, k, v = get_slot(aMap, key) 
	
	if i >= 0:
		bucket[i] = (key, value)#赋值为元组，类似列表，但是其内容不能修改，可删除
	else:
		bucket.append((key, value))#不加括号就是两个值，加了括号才是一个值

def delete(aMap, key):
	bucket = get_bucket(aMap, key)
	
	for i in xrange(len(bucket)):#xrange类似与range，不过是生成器，list(xrange())=range()
		k, v = bucket[i]
		if key == k:
			del bucket[i]#删除列表中的对应值
			break#中断循环

def list(aMap):
	for bucket in aMap:
		if bucket:
			for k, v in	bucket:
				print k, v 

