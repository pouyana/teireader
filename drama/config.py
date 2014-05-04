#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from drama import Drama
drama = Drama("machine_classified_corrected/Vom verfolgten Lateiner.out.xml")
casts = drama.get_cast()
print casts
scene = drama.get_scene()
for s in scene:
	for c in s:
		print c.tag
stages = drama.get_stage_all()
print stages
for stage in stages:
    if (stage["type"] in ["enter","exit"]):
        speakers = stage["text"].split(".")
        for spk in speakers:
            for cast in casts:
                my_regex = re.escape(cast["name"])
                print my_regex
                print re.search(my_regex,spk,re.IGNORECASE)
