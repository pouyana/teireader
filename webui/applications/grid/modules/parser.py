#!/usr/bin/env python
# -*- coding: utf-8 -*-
from drama import Drama
the_drama =  Drama('files/stranitzky_tuerk.xml')
#test the file properties.
print the_drama.get_title()
print the_drama.get_bibl_title()
print the_drama.get_bibl_author()
print the_drama.get_publish_data()["license"]
print the_drama.get_creation_date()
