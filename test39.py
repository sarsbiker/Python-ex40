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
#逐一打印，某某缩写后是某某
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
#逐一打印，某某州有某某城市
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)
#逐一打印，某某的缩写是啥，且有某某城市
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])

print '-' * 10
state = states.get('Texas')#取出states中Texas的值

if not state:#如果state没有取到结果
	print "Sorry, no Texas."

city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
