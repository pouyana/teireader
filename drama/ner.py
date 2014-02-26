# -*- coding: utf-8 -*-
'''

'''
import nltk.data
import pickle
import re
from drama import Drama

def extract_entities(text):
	entities = []
	for sentence in sent_tokenize(text):
	    chunks = ne_chunk(pos_tag(word_tokenize(sentence)))
	    print tokenize.WordPunctTokenizer().tokenize(sentence)
	return chunks
