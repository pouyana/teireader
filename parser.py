#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

tree = ET.parse('files/LessiMinna_von_BaDrame.xml')
root = tree.getroot()
print root.tag