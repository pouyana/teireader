# -*- coding: utf-8 -*-
'''

'''
from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk, tokenize


def extract_entities(text):
	entities = []
	for sentence in sent_tokenize(text):
	    chunks = ne_chunk(pos_tag(word_tokenize(sentence)))
	    print tokenize.WordPunctTokenizer().tokenize(sentence)
	return chunks


if __name__ == '__main__':
	text = """
	Orsanes und Elmira treten ab.
"""
	print extract_entities(text)
