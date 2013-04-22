#/usr/bin/python
#coding:utf-8

import sys,os
import json
import couchdb

dbname=os.path.basename(sys.argv[1].split('.')[0])

server=couchdb.Server('http://127.0.0.1:5984')
#db=server.create(dbname)
db=server[dbname]

docs=json.loads(open(sys.argv[1]).read())
db.update(docs,all_or_nothing=True)
