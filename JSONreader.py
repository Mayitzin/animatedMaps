# -*- coding: utf-8 -*-
"""
JSON reader

@author: Mario Garcia
www.mayitzin.com
"""

import json
import simplejson

fileName = './data/mexbdy.json'

# Read JSON trsing from file and convert into Dictionary
with open(fileName, 'r') as f:
	json_data = json.load(f)

print "File",fileName,"is now",type(json_data)

print json_data.keys()

print len(json_data['objects'])
print json_data['objects'].keys()
print json_data['objects']['mexbdy'].keys()
print json_data['objects']['mexbdy']['geometries'][0]
print type(json_data['objects']['mexbdy']['geometries'])