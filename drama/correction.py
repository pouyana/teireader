#!/usr/bin/env python
# -*- coding: utf-8 -*-

from drama import Drama
from tools import Tools
import os
import re
import json

def find_xml(txtfile):
    xml_file_name = txtfile.strip(".txt")+".out.xml"
    return xml_file_name

tools = Tools()
files_dir = "corfiles"
file_list = os.listdir(files_dir)
cn = 0
stats={}
for f in file_list:
    if(re.match(".*\.txt",f)):
        print f
        xml_file = files_dir+"/"+find_xml(tools.unicode_safe(f))
        xml = Drama(xml_file)
        tree = xml.get_tree()
        title = xml.get_title()
        save_file = files_dir+"/"+title+".cor.xml"
        lines = [line.strip() for line in open(files_dir+"/"+f)]
        for line in lines:
            jsondata = json.loads(line)
            stage = xml.get_content_by_id(jsondata["id"])
            if("type" in stage.attrib):
                if(stage.attrib["type"]!=jsondata["type"]):
                    stats[(stage.attrib["type"],jsondata["type"])] = stats.setdefault((stage.attrib["type"],jsondata["type"]))+1
            #else:
            #    stage.set("type",jsondata["type"])
