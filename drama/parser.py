#!/usr/bin/env python
# -*- coding: utf-8 -*-
from drama import Drama
from ner import Ner
from tools import Tools
import os
import re
#the_drama =  Drama('files/LessiDer_MisogynDrame.xml')
tools = Tools()
ner = Ner()
files_dir = "hand_classified"
dirprefix = "corpora/"
file_prefix = "cv"
file_list = os.listdir(files_dir)
cn = 0
for f in file_list:
    the_drama = Drama(files_dir+"/"+f)
#    print the_drama.get_title()
#print the_drama.get_bibl_title()
#print the_drama.get_bibl_author()
#print the_drama.get_publish_data()["license"]
#print the_drama.get_creation_date()
#print the_drama.get_fix_stage()
    stages = the_drama.get_stage_all()
    for x in stages:
        if not os.path.exists(dirprefix+x):
            os.makedirs(dirprefix+x)
        for directive in stages[x]:
            if(directive):
                #if the directive actually contains words.
                if(re.match("\w+",directive)):
                    if(not ner.only_names(tools.unicode_safe(directive))):
                        print x+"==>"+tools.unicode_safe(directive)
                        file_handle = open(dirprefix+x+"/"+file_prefix+str(cn),"w")
                        file_handle.write(tools.unicode_safe(directive))
                        file_handle.close()
                        cn = cn + 1
    print "finished"
