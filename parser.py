#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from drama import Drama

tree = ET.parse('files/LessiMinna_von_BaDrame.xml')
root = tree.getroot()
id = root.attrib['{http://www.w3.org/XML/1998/namespace}id']
name = root.attrib['n']
drama = Drama(id,name)
print drama.title