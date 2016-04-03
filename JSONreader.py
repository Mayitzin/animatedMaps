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