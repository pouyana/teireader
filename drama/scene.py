#!/usr/bin/env python
# -*- coding: utf-8 -*-
from drama import Drama
import re
import xml.etree.ElementTree as ET
from tools import Tools

def search(tokenized_text, tokenized_cast):
    all_cast = tokenized_cast
    result = {"status":False,"found":[]}
    for text in tokenized_text:
        if text in all_cast:
            result["status"]=True
            result["found"].append(text)
    return result

drama = Drama("hand_classified/LessiDer_FreigeisDrame.xml")
tools = Tools()
casts = drama.get_cast()
tokenized_cast = [re.findall("\w+",elem["name"]) for elem in casts]
all_cast = []
tree = drama.get_tree()
#parent_map = dict((c, p) for p in tree.getiterator() for c in p)
#print parent_map
count = 0
for cast in tokenized_cast:
    all_cast = all_cast + cast
for scene in set(drama.get_scene()):
    print scene.tag
    print scene.attrib
    count = count + 1
    tmp_element = ET.Element("config")
    tmp_element.set("num",str(count))
    for elem in scene.iter():
        if elem is not scene:
		tmp_element.append(elem)	
    scene.clear()
    scene.append(tmp_element)
    #print "===="
    #parent_map = dict((c.tag,p.tag) for p in scene.getiterator() for c in p)
    #print parent_map
    #print "===="
    #for p in scene.getiterator():
    #config.extend(p)
    stages = [elem for elem in scene.iter(drama.ns_tei+"stage") if elem is not scene]
    for stage in stages:
	stage_type = drama.get_stage_type(stage)
        stage_text = drama.get_stage_text(stage)
	#if(stage_type in ["enter","exit"]):
		#if stage_type == "enter":
			#for cast in all_cast:
			#	if (cast in stage_text.split()):
			#		print casts
tree.write("out.xml")
