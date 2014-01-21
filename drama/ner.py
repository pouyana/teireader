# -*- coding: utf-8 -*-
'''

'''
from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk, tokenize
from drama import Drama

def extract_entities(text):
	entities = []
	for sentence in sent_tokenize(text):
	    chunks = ne_chunk(pos_tag(word_tokenize(sentence)))
	    print tokenize.WordPunctTokenizer().tokenize(sentence)
	return chunks


if __name__ == '__main__':
    text = Drama("files/Horribilicribrifax.xml")
    collection_a = text.get_stage_all()
    test_text = "".join(str(x) for x in collection_a["enter"])
    print extract_entities(test_text)
