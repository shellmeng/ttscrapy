#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
s=u'孟'

print s

f=open('t.txt','w+')
f.write(s.decode('utf-8'))
