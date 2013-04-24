# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

#coding:utf-8
import sys

import json
import couchdb
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
class file2json(object):
    	def __init__(self):
		self.file=open('newsfromsina.txt','w+')
	#	self.server=couchdb.Server('http://127.0.0.1:5984')
	#	try:
	#		self.db=self.server.create("sports")
	#	except:
	#		pass
	#	self.db=self.server["sports"]

	def process_item(self, item, spider):
		itemdic={}
		#w=(item['title'][0].decode("unicode_escape"))
		#itemdic['title']=w
		#itemdic['body']=[]
		#if(len(item['body'])>0):
		#	for b in item['body']:
		#		itemdic['body'].append(b.decode("unicode_escape"))
		
		itemdic['title']=item['title']
		itemdic['body']=item['body']
		out=json.dumps(itemdic, ensure_ascii=False)
	#	self.db.update(json.loads(out.encode('utf-8')))
		self.file.write(out)
		self.file.write(",\n")
		#self.file.write(out)
		#self.file.write('\n')


class fileStore(object):

    	def __init__(self):
		self.file=open('newsfromsina.txt','w+')


	
	def process_item(self, item, spider):

		print 'the item is '+'*'*15
		print item

		#print 

		s=""
		b=""
		try:
			s=item['title'][0]
			self.file.write(s.decode('utf-8'))
			self.file.write('\n')

			for b in item['body']:
				self.file.write(b.decode('utf-8'))
				self.file.write('\n')
			self.file.write('\n')
			self.file.write('\n')
		except IndexError:
			pass

		print 'the s is '+s+'*'*15
		print 'the b is '+b+'*'*15
		#y=s.encode('utf-8')
		#print y.join('\n')
		#t=y.join('\n')
		#print 'the t is '+t+'*'*15

		print 'yes'+'*'*100
        	#return item
