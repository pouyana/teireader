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
files_dir = "machine_classified_corrected"
file_list = os.listdir(files_dir)
cn = 0
stats={}
for f in file_list:
    if(re.match(".*\.txt",f)):
#        print f
        xml_file = files_dir+"/"+find_xml(tools.unicode_safe(f))
        xml = Drama(xml_file,"WARNING")
        tree = xml.get_tree()
        title = xml.get_title()
        save_file = files_dir+"/"+title+".cor.xml"
        lines = [line.strip() for line in open(files_dir+"/"+f)]
        for line in lines:
#            print line
            jsondata = json.loads(line)
#            print xml.get_content_by_id("tg123.2")
            stage = xml.get_content_by_id(jsondata["id"])
            if(stage is not None):
                if("type" in stage.attrib):
                    if(stage.attrib["type"]!=jsondata["type"]):
                        print tools.unicode_safe(stage.attrib["type"]) +"==>"+tools.unicode_safe(jsondata["type"])+"||"+tools.unicode_safe(jsondata["text"])
                        if(not (stage.attrib["type"],jsondata["type"]) in stats):
                            stats.setdefault((stage.attrib["type"],jsondata["type"]))
                            stats[(stage.attrib["type"],jsondata["type"])]=1
                        else:
                            stats[(stage.attrib["type"],jsondata["type"])]=stats[(stage.attrib["type"],jsondata["type"])]+1


print "corrections:\n"
print "|    Before  |   After   |   Count    |"
for st,vals in stats.iteritems():
    print "|    "+st[0]+"   |   "+st[1]+"  |    "+str(vals)+"   |"
