#/usr/bin/python
#coding:utf-8

import sys,os
import json
import couchdb
import codecs
from couchdb import Document 
import types


print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
           key = key.encode('utf-8')
        if isinstance(value, unicode):
           value = value.encode('utf-8')
        elif isinstance(value, list):
           value = _decode_list(value)
        elif isinstance(value, dict):
           value = _decode_dict(value)
        rv[key] = value
    return rv



dbname=os.path.basename(sys.argv[1].split('.')[0])

server=couchdb.Server('http://127.0.0.1:5984')
try:
	db=server.create(dbname)
except:
	pass
db=server[dbname]
line=(codecs.open(sys.argv[1],'r','utf-8').read())

docs=json.loads(line.encode('utf-8'))#,object_hook=_decode_dict)
db.update(docs)
#for l in line.split('\n'):
#	docs=json.loads(l)#,object_hook=_decode_dict)
#	print docs
#	db.update(docs)

#d={}

#db.update(d)

