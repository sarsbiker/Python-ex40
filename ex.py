#coding=gb2312
import requests
 
r = requests.get('http://cuiqingcai.com')
print type(r)
print r.status_code
print r.encoding
#print r.text
print r.cookies