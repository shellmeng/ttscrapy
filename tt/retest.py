import re

s=',comma'
#s='www.baidu.comaa'

rule=r'com*'

re.compile(rule)
m=re.findall(rule,s)
#m=re.match(rule,s)
print m
