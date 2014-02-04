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
    classifier = pickle.load(open("grid_sklearn.RandomForestClassifier.with.enter.pickle"))
#    print text.get_fix_stage()
    collection_a = text.get_fix_stage()

    temp=[]
    tree = text.get_tree()
    title = text.get_title()
    file_handle = open("mcfiles/"+title+".txt","w")
    for c in collection_a:
        if("text" in c):
            stage = {}
            stage["text"]=c["text"]
            stage["id"]=c["id"]
            if(c["text"]):
                c = re.sub('\.$', '', stage["text"])
                words = re.findall('(\S+)',c)
                feats = dict([(word, True) for word in words])
                stage["type"]=classifier.classify(feats)
                temp.append(stage)
                classification = None
    for a in temp:
        stage = text.get_content_by_id(a["id"])
        stage.set("type",a["type"])
        file_handle.write(a["id"]+": "+a["text"]+"  ==> "+a["type"]+"\n")
        print a["id"]+": "+a["text"]+" ==> "+a["type"]
    tree.write("mcfiles/"+text.get_title()+".out.xml")
    file_handle.close()
    #n=["Sara", "und","Mat","Gehen","ab"]
    #feats = dict([(word, True) for word in n])
    #print classifier.classify(feats)
