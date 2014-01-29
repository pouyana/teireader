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


if __name__ == '__main__':
    text = Drama("ncfiles/WeiseMasanielloDrame.xml")
    classifier = pickle.load(open("grid_sklearn.RandomForestClassifier.pickle"))
#    print text.get_fix_stage()
    collection_a = text.get_fix_stage()

    temp=[]
    for c in collection_a:
        if(c):
            stage = {}
            stage["text"]=c
            c = re.sub('\.$', '', c)
            words = re.findall('(\S+)',c)
            feats = dict([(word, True) for word in words])
            stage["type"]=classifier.classify(feats)
            temp.append(stage)
            #classification = None
    for a in temp:
        print a["text"]+" ==> "+a["type"]
#    n=["Geht","ab"]
#    feats = dict([(word, True) for word in n])
#    print classifier.classify(feats)

