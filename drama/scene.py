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
print casts
tokenized_cast = [re.findall("\w+",elem["name"]) for elem in casts]
all_cast = []
tree = drama.get_tree()
for cast in tokenized_cast:
    all_cast = all_cast + cast
for scene in drama.get_scene():
    config = ET.Element("config")
    stages = [elem for elem in scene.iter(drama.ns_tei+"stage") if elem is not scene]
    for stage in stages:
        d = ET.SubElement(a)
        if ("type" in stage.attrib):
            stage_type = stage.attrib["type"]
            if(stage_type in ["enter","exit"]):
                if(re.match("\S+",stage.text.rstrip().lstrip())):
                    if stage_type == "enter":
                        tokenized_text = re.findall("\w+",tools.normalize_text(stage.text))
                        if search(tokenized_text,all_cast)["status"]:
                            print "a"
                else:
                    for elem in stage:
                        if (elem.text and stage_type=="enter"):
                            tokenized_text = re.findall("\w+",tools.normalize_text(elem.text))
                            if search(tokenized_text,all_cast)["status"]:
                                print "a"
tree.write("aout.xml")
