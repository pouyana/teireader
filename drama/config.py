#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from drama import Drama
drama = Drama("machine_classified_corrected/Vom verfolgten Lateiner.out.xml")
casts = drama.get_cast()
stages = drama.get_stages_with_type()
for stage in stages:
    if (stage["type"] in ["enter","exit"]):
        speakers = stage["text"].split(".")
        for spk in speakers:
            for cast in casts:
                my_regex = re.escape(cast["name"])
                print my_regex
                print re.search(my_regex,spk,re.IGNORECASE)
