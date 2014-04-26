#!/usr/bin/env python
# -*- coding: utf-8 -*-
from drama import Drama
import re
import xml.etree.ElementTree as ET
from tools import Tools
drama = Drama("hand_classified/LessiDer_FreigeisDrame.xml")
tools = Tools()
scene = drama.get_scene()
for s in scene:
    print s.attrib
