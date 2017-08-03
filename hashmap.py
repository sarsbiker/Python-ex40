#coding=utf-8
def new(num_buckets=1):#����������Ĭ��ֵ��������õ�ʱ��û����ֵ�ͻ�ʹ��Ĭ�ϵ�
	aMap = []
	for i in range(0,num_buckets):
		aMap.append([])#�б�ĩβ���ӿ��С�����֮����[[],[]]
	return aMap

def hash_key(aMap, key):
	return hash(key) % len(aMap)# %��ʾ��������ǡ���Ǳ����Ļ��ͻ��0
	#hash() ���ڻ�ȡȡһ�������ַ���������ֵ�ȣ��Ĺ�ϣֵ�����صľ��� һ�α��룬�������֣�Ψһ

def get_bucket(aMap, key):
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]#ȡ���б���Ķ�Ӧ��Ԫ�أ���Ȼ���б����Ƕ�ά�Ķ��ж��б�

def get_slot(aMap, key, default=None):
	bucket = get_bucket(aMap, key)#���ݶ�Ӧ�ļ�����˵�ֶ�ĳһ�У�ȡ��Ӧֵ��Ҳ����ѡ��ĳһ��
	
	for i,kv in enumerate(bucket):#���������б��н�����Ա��Ƿ��Ѵ���
		#enumerate() �������ڽ�һ���ɱ��������ݶ���(���б�Ԫ����ַ���)���Ϊһ���������У�ͬʱ�г����ݺ������±�
		k, v = kv#��ֵƥ��
		if key == k:#�������ļ��Ѿ�����
			return i, k, v #�����������֣�����ֵ
			#���������������
	return -1, key, default#���ؽ��Ϊ��

def get(aMap, key, default=None):
	i, k, v = get_slot(aMap, key, default=default)
	return v #��������ļ���ȡ��Ӧ��ֵ��ֻ����ֵ

def set(aMap, key, value):
	bucket = get_bucket(aMap, key)#
	i, k, v = get_slot(aMap, key) 
	
	if i >= 0:
		bucket[i] = (key, value)#��ֵΪԪ�飬�����б����������ݲ����޸ģ���ɾ��
	else:
		bucket.append((key, value))#�������ž�������ֵ���������Ų���һ��ֵ

def delete(aMap, key):
	bucket = get_bucket(aMap, key)
	
	for i in xrange(len(bucket)):#xrange������range����������������list(xrange())=range()
		k, v = bucket[i]
		if key == k:
			del bucket[i]#ɾ���б��еĶ�Ӧֵ
			break#�ж�ѭ��

def list(aMap):
	for bucket in aMap:
		if bucket:
			for k, v in	bucket:
				print k, v 

