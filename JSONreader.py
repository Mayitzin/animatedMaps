# -*- coding: utf-8 -*-
"""
JSON reader

@author: Mario Garcia
www.mayitzin.com
"""

import json
import simplejson

fileName = './data/mexbdy.json'
# fileName = './data/Municipios_2010_5A.json'

# Read JSON trsing from file and convert into Dictionary
with open(fileName, 'r') as f:
    json_data = json.load(f)

def printProperties(json_data, state_number=0):
    print json_data['objects']['mexbdy']['geometries'][state_number]['type']
    listProps = json_data['objects']['mexbdy']['geometries'][state_number]['properties'].keys()
    for prop in listProps:
        print "   ", prop, "=", json_data['objects']['mexbdy']['geometries'][state_number]['properties'][prop]

def listStates(json_data):
    states_list = []
    n = len(json_data['objects']['mexbdy']['geometries'])
    for i in range(n):
        states_list.append(json_data['objects']['mexbdy']['geometries'][i]['properties']['DESCRIP'])
    return states_list

def listMunicipalities(json_data):
    municipality_list = []
    n = len(json_data['objects']['Municipios_2010_5A']['geometries'])
    for i in range(n):
        municipality_list.append(json_data['objects']['Municipios_2010_5A']['geometries'][i]['properties']['NOM_MUN'])
    return municipality_list


# List States
print listStates(json_data)

# List Municipalities
municList = listMunicipalities(json_data)
print "There are", len(municList), "Municipalities listed"

repeated = {}
for municipality in municList:
    amount = municList.count(municipality)
    if amount>1: repeated[municipality] = amount

print len(repeated), "municipalities are repeated"
