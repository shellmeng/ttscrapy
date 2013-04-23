#coding:utf-8
#!/usr/bin/python

import jieba


text=open("../newsfromsina.txt").read()
seg_list=jieba.cut(text);
print "###".join(seg_list)
