#!/usr/bin/env python
# -*- coding: utf-8 -*-
#the code has extentive use of xPath.
import xml.etree.ElementTree as ET
class Drama:
	#root = None
	"""Drama Self Class, which contain description and common data of a drama file."""
	prefix = "{http://www.tei-c.org/ns/1.0}"
	def __init__(self,text_file):
		self.text_file = text_file
		self.import_xml()

	def import_xml(self):
		tree = ET.parse(self.text_file)
		root = tree.getroot()
		self.set_root(root)
	
	def set_root(self,root):
		self.root = root
	
	def get_root(self):
		return self.root

	def get_all_parent(self,element):
		parent = self.root.findall(".//"+element.tag+"/..")
		return parent

	def get_first_parent(self,element):
		parent = self.root.find(".//"+element.tag+"/..")
		return parent

	def get_first_child(self,element):
		child = self.root.find(".//"+element.tag+"/*")
		return child
	
	def get_all_child(self,element):
		child = self.root.findall(".//"+element.tag+"/*")
		return child
	#search a list for a tag
	def find_by_tag(self,lst,tag):
		for element in lst:
			if(hasattr(element,"tag")):
				if(element.tag==tag):
					return element
	#get book title from the header files.
	def get_title(self):
		fDs = self.root.findall(".//"+self.prefix+"fileDesc/"+self.prefix+"titleStmt/"+self.prefix+"title")
		return fDs[0].text
	#get fullbibliography of a title.
	def get_bibl_title(self):
		fDs = self.root.findall(".//"+self.prefix+"biblFull/"+self.prefix+"titleStmt/"+self.prefix+"title")
		return fDs[0].text

	def get_bibl_author(self):
		fDs = self.root.findall(".//"+self.prefix+"biblFull/"+self.prefix+"titleStmt/"+self.prefix+"author")
		author = {"name":fDs[0].text,"pnd":fDs[0].attrib["key"]}
		return author



