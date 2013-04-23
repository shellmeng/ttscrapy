#!/usr/bin/python

import couchdb
import os,sys

try:
	import jsonlib2 as json
except:
	import json

db=os.path.basename(sys.argv[1]).split('.')[0]



server=couchdb.Server('http://localhost:5984')
try:
	db=server.create(db)

except:
	pass

docs=json.loads(open(sys.argv[1]).read())
db.update(docs,all_or_nothing=True)
