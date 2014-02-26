# -*- coding: utf-8 -*-
import nltk.data
from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk, FreqDist
import pickle
import re
from drama import Drama

def extract_entities(text):
    entities = []
    words = word_tokenize(text)
    chunks = ne_chunk(pos_tag(words))
    entities.extend([chunk for chunk in chunks if hasattr(chunk, 'node')])
    return entities

text = Drama("ncfiles/WeiseMasanielloDrame.xml")
collection_a = text.get_fix_stage()
for c in collection_a:
        if("text" in c):
            stage = {}
            stage["text"]=c["text"]
            stage["id"]=c["id"]
            if(c["text"]):
		#find all the words in the sentence
		text_words = re.findall("\w+",c["text"])
		#named entity recognition
		entities = extract_entities(c["text"].rstrip('\r\n'))
		name_list = []
		for entitiy in entities:
			name_list.append(entitiy[0][0])
		#see ordered list / unodered lists.
		if (set(text_words)==set(name_list)):
			print c["text"]
