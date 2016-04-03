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

def printProperties(json_data, state_number=0):
	print json_data['objects']['mexbdy']['geometries'][state_number]['properties'].keys()

def listStates(json_data):
	states_list = []
	n = len(json_data['objects']['mexbdy']['geometries'])
	for i in range(n):
		states_list.append(json_data['objects']['mexbdy']['geometries'][i]['properties']['DESCRIP'])
	return states_list

print json_data.keys()

print len(json_data['objects'])
print json_data['objects'].keys()
print json_data['objects']['mexbdy'].keys()
print len(json_data['objects']['mexbdy']['geometries'])
print listStates(json_data)