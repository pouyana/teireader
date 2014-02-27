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

text1="Selenissa Horribilicribrifax Harpax"

text = Drama("files/Horribilicribrifax.xml")
collection_a = text.get_fix_stage()
for c in collection_a:
        if("text" in c):
            stage = {}
            stage["text"]=c["text"]
            stage["id"]=c["id"]
            if(c["text"]):
		#find all the words in the sentence
		text_words = re.findall("\w+",c["text"])
		#print text_words
		#named entity recognition 
		#there is problem with dots so I remove them.
		#I know that I send only on sentence to the entity recognizer
		normilized_string = c["text"].replace(".","")
		entities = extract_entities(normilized_string)
		#print entities
		name_list = []
		for entitiy in entities:
			for names in entitiy:
				name_list.append(names[0])
		#see ordered list / unodered lists.
		#print c["text"]
		if (set(text_words)==set(name_list)):
			print c["text"]
