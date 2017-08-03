#coding=utf-8
states = {
	'Oregon':'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY State has:", cities['NY']#new york
print "OR state has:", cities['OR']#portland

print '-' * 10
print "Michigan's abbreviation is:", states['Michigan']#mi 
print "Florida's abbreviation is:", states['Florida']#fl 

print '-' * 10
print "Michigan has:", cities[states['Michigan']]#detroit
print "Florida has:", cities[states['Florida']]#jacksonville
#��һ��ӡ��ĳĳ��д����ĳĳ
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
#��һ��ӡ��ĳĳ����ĳĳ����
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)
#��һ��ӡ��ĳĳ����д��ɶ������ĳĳ����
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])

print '-' * 10
state = states.get('Texas')#ȡ��states��Texas��ֵ

if not state:#���stateû��ȡ�����
	print "Sorry, no Texas."

city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
