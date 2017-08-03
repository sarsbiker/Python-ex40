#coding=utf-8
formatter = "%r %r %s %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % ("一","二","三","四")#%r 不能打印出中文，还是得s
print formatter % (True,False,True,False)#自带的布尔值，不需要引号
print formatter % (formatter,formatter,formatter,formatter)#r代表的是原始值
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",#逗号不要忘记咯，连接
	"So I said goodnight."
)