#!/usr/bin/env python
# -*- coding: utf-8 -*-
from drama import Drama
the_drama =  Drama('files/newBosteDer_hochm_tiLibre.xml')
#test the file properties.
#print the_drama.get_title()
#print the_drama.get_bibl_title()
#print the_drama.get_bibl_author()
#print the_drama.get_publish_data()["license"]
#print the_drama.get_creation_date()
print the_drama.get_fix_stage()
