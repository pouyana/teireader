#!/usr/bin/env python
# -*- coding: utf-8 -*-
#the named entity recognition module using socket to connect 
#stanford ner and pos_tag servers

import re
from nltk import word_tokenize,ne_chunk,pos_tag
from nlp_socket import NLPSocket
from drama import Drama
import xml.etree.ElementTree as ET

class Ner:
    #two methods can be used to extract entites
    #using the nlp of stanford

    def get_ner(self,text):
        #change the server to your own.
        ner_socket = NLPSocket("192.168.1.28",9191)
        data = ner_socket.recv_data(text)
        return data

    def get_pos(self,text):
        #change the server to your own.
        pos_socket = NLPSocket("192.168.1.28",9192)
        data = pos_socket.recv_data(text)
        return data

    def only_names(self,text):
        #text = text.replace("\n","")
        #text = text.replace("\r","")
        text = text.strip()
        result = False
        if(len(re.findall("\w+",text))<32):
            text = re.sub('[.!;]',",",text)
            xml_pos = self.get_pos(text)
            #print xml_pos
            root = ET.fromstring(xml_pos)
            name_count=0
            only_names = True
            for child in root.iter("word"):
                if(re.match("^NE$",child.attrib["pos"])):
                    name_count = name_count + 1
                if(re.match("(VV.*|PTK.*|PPER|ADV|APPR)",child.attrib["pos"])):
                    only_names = False
            if(name_count > 0 and only_names):
                result = True
        return result

    #using nltk
    def extract_entities(self,text):
        entities = []
        words = word_tokenize(text)
        chunks = ne_chunk(pos_tag(words))
        entities.extend([chunk for chunk in chunks if hasattr(chunk, 'node')])
        return entities

    def all_names(self,text):
        words = re.findall("\w+",text)
        normalized_string = text.replace(".",",")
        entities = self.extract_entities(normalized_string)
        name_list =[]
        for entitiy in entities:
            for name in entitiy:
                name_list.append(name[0])
        if (set(words)==set(name_list)):
            return True
#test case
#text = Drama("files/LessiNathan_der_WDrame.xml")
#ner = Ner()
#collection_a = text.get_fix_stage()
#for c in collection_a:
#        if("text" in c):
#            stage = {}
#            stage["text"]=c["text"]
#            stage["id"]=c["id"]
#            c["text"] = "Herr Oronte. Frau Oronte. von Schlag. Peter. Lelio. Lisette. Herr Kräusel. Jungfer Ohldin."
#            if(c["text"]):
#                if(re.match("\w+",c["text"])):
#                    if(ner.only_names(c["text"])):
#                        print c["id"]+"===>"+c["text"]
