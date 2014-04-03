#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
import re
from logger import Logger
from speech import Speech, SpeakerStatistics, SpeakerStatisticsCollection
from tools import Tools
class Drama:
        """
        Handles the data extraction from TEI xml data. It uses ElementTree bulit-in class from python.Setting log_level is
        optional and the default value is ``ERROR``.
        To use the Drama class just use the following code:

        .. code-block:: python

            from drama import Drama
            drama = Drama (xml_file_address,[log_level])

        """
        ns_tei = "{http://www.tei-c.org/ns/1.0}"
        ns_w3 = "{http://www.w3.org/XML/1998/namespace}"

        def __init__(self,xml_data,log_level="ERROR"):
            logger = Logger(log_level)
            self.log = logger.get_logger()
            self.xml_file = xml_data
            self.import_xml()

        def import_xml(self):
            """
            Imports, parses XML and adds local tree and root objects. It is mandatory for initiating. Raises ``ERROR`` if not working properly.
            """
            try:
                tree = ET.parse(self.xml_file)
                root = tree.getroot()
                self.set_root(root)
                self.set_tree(tree)
            except ParseError as pe:
                self.log.error("Parsing ErrorNr:"+ str(pe.code) +" at the Position "+ str(pe.position)+".")
                raise

        def set_tree(self,tree):
            """
            Sets the elements tree, needs tree object which is the result of ET.parse, if tree not ElementTree, returns ``None``.
            Logs as ``ERROR``
            """
            if (type(tree).__name__ == "ElementTree"):
                self.tree = tree
            else:
                self.log.error("The Object given was not ElementTree, please check.")
                self.tree = None
                raise

        def get_tree(self):
            """
            Returns elements tree of a XML data. When not sent returns ``None``.
            """
            if self.tree:
                return self.tree
            else:
                return None

        def set_root(self,root):
            """
            Sets the root element of XML data. The root element must be ElementTree Element. When not set to ``None``.
            """
            if (type(root).__name__=="Element"):
                self.root = root
            else:
                self.root = None

        def get_root(self):
            """
            Returns the root element of an XML data. Not finding root returns ``None``.
            """
            if (self.root):
                return self.root
            else:
                return None

        def get_title(self):
            """
            Returns the Drama title, which is set in XML data. can be used to better name display in webpages.
            Return type is ``string`` or ``None`` when not found the error is logged as ``WARNING``.
            """
            try:
                fDs = self.root.findall(".//"+self.ns_tei+"fileDesc/"+self.ns_tei+"titleStmt/"+self.ns_tei+"title")
                return fDs[0].text
            except IndexError as e:
                self.log.warning("title element not found.")

        def get_bibl_title(self):
            """
            Returns bibliographic title of Drama. Returns string if bibl_title found, if not gives a ``WARNING``.
            """
            try:
                fDs = self.root.findall(".//"+self.ns_tei+"biblFull/"+self.ns_tei+"titleStmt/"+self.ns_tei+"title")
                return fDs[0].text
            except IndexError as e:
                self.log.warning("bibl title not found.")

        def get_bibl_author(self):
            """
            Return the author of the drama, with the pnd number. Returns collections. When not finding anything returns None with ``WARNING``

            .. code-block:: python

                {"name":string,"pnd":integer}

            """
            try:
                fDs = self.root.findall(".//"+self.ns_tei+"biblFull/"+self.ns_tei+"titleStmt/"+self.ns_tei+"author")
                author = {"name":fDs[0].text,"pnd":fDs[0].attrib["key"]}
                return author
            except IndexError:
                self.log.warning("could not find the name.")
                return None
            except AttributeError:
                self.log.warning("could not find the pnd number.")
                return None

        def get_license(self):
            """
            Returns the license of the drama Text. Return type is string.
            If not found retruns None and a ``WARNING``.
            """
            try:
                fDs = self.root.findall(".//"+self.ns_tei+"fileDesc/"+self.ns_tei+"publicationStmt/"+self.ns_tei+"availability/"+self.ns_tei+"p")
                return fDs[0].text
            except IndexError as e:
                self.log.warning("could not find license information.")
                return None

        def get_publish_data(self):
            fDs_date = self.root.findall(".//"+self.ns_tei+"biblFull/"+self.ns_tei+"publicationStmt/"+self.ns_tei+"date")
            fDs_place = self.root.findall(".//"+self.ns_tei+"biblFull/"+self.ns_tei+"publicationStmt/"+self.ns_tei+"pubPlace")
            data = {"date":fDs_date[0].attrib["when"],"place":fDs_place[0].text,"license":self.get_license()}
            return data

        #creation date
        #to do try/catch for the unkwnown attribs and also work with the existing attrib. less static more dynamic
        def get_creation_date(self):
            fDs = self.root.findall(".//"+self.ns_tei+"profileDesc/"+self.ns_tei+"creation/"+self.ns_tei+"date")
            data = {"after":fDs[0].attrib["notBefore"],"before":fDs[0].attrib["notAfter"]}
            return data
        #get the whole cast from the tei data.
        def get_cast(self):
            fDs = self.root.findall(".//"+self.ns_tei+"castItem")
            result = []
            for f in fDs:
                res ={"id":f.attrib[self.ns_w3+"id"],"name":f.text}
                result.append(res)
                return result

        #get fix-stage stuff
        def get_fix_stage(self):
            tool = Tools()
            fDs = self.root.findall(".//"+self.ns_tei+"stage")
            result = []
            for f in fDs:
                if(f.attrib):
                    tmp_stage={}
                    tmp_stage["id"]=f.attrib[self.ns_w3+"id"]
                    for c in f:
                        #a fix for stage in stage.
                        if(not(c.tag==self.ns_tei+"stage")):
                            tmp_stage["text"]=tool.unicode_safe(c.text)
                        if(f.text):
                            if(re.match("\S+",f.text)):
                                tmp_stage["text"]=tool.unicode_safe(f.text)
                                result.append(tmp_stage)
            return result
        #find act or scene
        def get_stages_with_type(self):
            stages=self.get_fix_stage()
            result = []
            for stage in stages:
                element = self.get_content_by_id(stage["id"])
                if "type" in element.attrib:
                    print element.attrib["type"]
                    stage["type"] = element.attrib["type"]
                    result.append(stage)
            return result

        def get_scene(self):
            fDs = self.root.findall(".//"+self.ns_tei+"div[@type='scene']")
            result = []
            for f in fDs:
                res ={"id":f.attrib[self.ns_w3+"id"],"name":f.attrib["n"]}
                result.append(res)
            return result

        #list all the ids, with this all of the acceable elements are found and can be used for further parsing
        def get_all_ids(self):
            fDs = self.root.findall(".//*[@"+self.ns_w3+"id]")
            result = []
            for f in fDs:
                res = f.attrib[self.ns_w3+"id"]
                result.append(res)
            return result


        def get_stage_all(self):
            """
            convert all stages to serialized collection, it can be used to create suitable corpora for the nltk-trainer.Returns:

            .. code-block:: python

                collection = {"enter":["kommt dazu!"],"exit":["Ab."],"dead":["Stribt."],"other":["singend."],"aside":["Ad Spect."]}

            """
            collection = {"enter":[],"exit":[],"dead":[],"other":[],"aside":[]}
            modes = ["enter","exit","dead","other","aside"]
            fDs = self.root.findall(".//"+self.ns_tei+"stage")
            for f in fDs:
                if ("type" in f.attrib):
                    if(f.attrib["type"] in modes and re.match('\S+',f.text)) :
                        collection[f.attrib["type"]].append(f.text)
                    elif(f.attrib["type"] in modes):
                        for c in f:
                            collection[f.attrib["type"]].append(c.text)
                else:
                    for c in f:
                        if("type" in c.attrib):
                            if(c.attrib["type"] in modes):
                                collection[c.attrib["type"]].append(f.text)
            return collection

        def get_content_by_id(self,ident):
            """
            id must be a alphanumeric value like tg123.2.
            Returns a Tree element for the given id. None if not found and a warning log.
            """
            try:
                fDs = self.root.findall(".//*[@"+self.ns_w3+"id='"+ident+"']")
                return fDs[0]
            except IndexError:
                self.log.warning("id"+ ident +"is not found.")
                return None

        #given speaker id get the <sp> tag which also contains <p> and <l> tags.
        def get_sp_by_speaker_id(self,ident):
            fDs = self.root.findall(".//*[@"+self.ns_w3+"id='"+ident+"']/..")
            if fDs:
                return fDs
            else:
                return None

        def get_all_speech_by_speaker(self,sp):
            result = []
            for child in sp:
                #if it is a <p> or <l> then put it in the result list
                if (child.tag == self.ns_tei+"p" or child.tag == self.ns_tei+"l"):
                    result.append(child)
                    if (child.tag == self.ns_tei+"lg"):
                        for c in child:
                            result.append(c)
            return result

        def get_all_speech(self):
            tools = Tools()
            fDs = self.root.findall(".//"+self.ns_tei+"speaker")
            result = []
            for f in fDs:
                if f.text is not None:
                    speaker = tools.unicode_safe(f.text)
                    speaker_id = f.attrib[self.ns_w3+"id"]
                    sps=self.get_sp_by_speaker_id(speaker_id)
                    for sp in sps:
                        speechs = self.get_all_speech_by_speaker(sp)
                        speech = Speech(speaker,speaker_id,speechs)
                        result.append(speech)
            return result

        def get_stats(self):
            spstats = SpeakerStatisticsCollection(self.get_all_speech())
            spstats.generate_stats()
            statistics = {}
            statistics["major"] = spstats.get_statistics()
            statistics["median_count"] = spstats.get_median_count()
            statistics["average_count"] = spstats.get_average_count()
            return statistics
