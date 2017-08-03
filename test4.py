#coding=utf-8
# 变量赋值
cars=100
space_in_a_car=4.0
drivers=30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
#打印结果
print '这里有',cars,'辆汽车'
print '我们有',drivers,'个司机'
print '所以还剩',cars_not_driven,'空车'
print '我们可以运输',carpool_capacity,'人'
print '这里有',passengers,'乘客'
print '我们需要安排每辆车',average_passengers_per_car,'乘客'
print 'hey %s there.'%'you'