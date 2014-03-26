#!/usr/bin/env python
# -*- coding: utf-8 -*-
from drama import Drama
from ner import Ner
from tools import Tools
import os
import re
import sys
tools = Tools()
ner = Ner()
import_files_dir = sys.argv[1]
export_files_dir = sys.argv[2]
files_dir = import_files_dir
dirprefix = export_files_dir
file_prefix = "cv"
file_list = None
if(os.path.isdir(files_dir) and os.path.isdir(dirprefix)):
    file_list = os.listdir(files_dir)
    cn = 0
if(file_list):
    for f in file_list:
        the_drama = Drama(files_dir+"/"+f)
        stages = the_drama.get_stage_all()
        for x in stages:
            if not os.path.exists(dirprefix+x):
                os.makedirs(dirprefix+x)
            for directive in stages[x]:
                if(directive):
                    if(re.match("\w+",directive)):
                        if(not ner.only_names(tools.unicode_safe(directive))):
                            print x+"==>"+tools.unicode_safe(directive)
                            file_handle = open(dirprefix+x+"/"+file_prefix+str(cn),"w")
                            file_handle.write(tools.unicode_safe(directive))
                            file_handle.close()
                            cn = cn + 1
    print "finished"
