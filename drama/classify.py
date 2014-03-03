# -*- coding: utf-8 -*-
'''

'''
import nltk.data
import pickle
import re
from ner import Ner
from drama import Drama

if __name__ == '__main__':
    text = Drama("ncfiles/LessiPhilotasDrame.xml")
    classifier = pickle.load(open("pickle/grid_sklearn.RandomForestClassifier.new.pickle"))
    collection_a = text.get_fix_stage()
    ner = Ner()
    temp=[]
    tree = text.get_tree()
    title = text.get_title()
    file_handle = open("mcfiles/"+title+".txt","w")
    for c in collection_a:
        if("text" in c):
            stage = {}
            stage["text"]=c["text"]
            stage["id"]=c["id"]
            stage["how"]=None
            if(c["text"] and re.match("\S+",c["text"])):
                c = re.sub('\.$', '', stage["text"])
                words = re.findall('(\S+)',c)
                if(ner.only_names(c)):
                        stage["type"]="enter"
                        stage["how"]="NLP"
                feats = dict([(word, True) for word in words])
                if(not stage.has_key("type")):
                    stage["type"]=classifier.classify(feats)
                    stage["how"]="nltk"
            temp.append(stage)
            classification = None
    for a in temp:
        stage = text.get_content_by_id(a["id"])
        if(a.has_key("type")):
            stage.set("type",a["type"])
            file_handle.write(a["id"]+": "+a["text"]+"  ==> "+a["type"]+" "+a["how"]+"\n")
            print a["id"]+": "+a["text"]+" ==> "+a["type"]+" "+a["how"]
    tree.write("mcfiles/"+text.get_title()+".out.xml")
    file_handle.close()
