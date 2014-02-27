# -*- coding: utf-8 -*-
from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk, FreqDist
import re
from drama import Drama
class Ner:
    def extract_entities(self,text):
        entities = []
        words = word_tokenize(text)
        chunks = ne_chunk(pos_tag(words))
        entities.extend([chunk for chunk in chunks if hasattr(chunk, 'node')])
        return entities

    def all_names(self,text):
        words = re.findall("\w+",text)
        normalized_string = text.replace(".","")
        entities = self.extract_entities(normalized_string)
        name_list =[]
        for entitiy in entities:
            for name in entitiy:
                name_list.append(name[0])
        if (set(words)==set(name_list)):
            return True
#test case
text = Drama("files/Horribilicribrifax.xml")
ner = Ner()
collection_a = text.get_fix_stage()
for c in collection_a:
        if("text" in c):
            stage = {}
            stage["text"]=c["text"]
            stage["id"]=c["id"]
            if(c["text"]):
                if(ner.all_names(c["text"])):
                    print c["text"]
