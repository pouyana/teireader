#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import re for the regex
import re
from tools import Tools
class Speech:
	"""Speech (Replik) class, which have the text, speaker and also the length of the speech."""
	def __init__(self,speaker,id,content):
		self.set_id(id)
		self.set_speaker(speaker)
		self.set_content(content)

	#output string print command
	def __str__(self):
		text = self.content_joiner()
		return "Speech of "+str(self.get_speaker())+" with the id "+str(self.get_id())+"\n" + str(self.get_length())

	#get the speaker name
	def get_speaker(self):
		return self.speaker
		
	#set the speaker name
	def set_speaker(self,speaker):
		self.speaker = speaker
		
	#set the speech id
	def set_id(self,id):
		self.id = id

	def get_id(self):
		return self.id

	#set the content of the speech
	def set_content(self,content):
		self.content = content

	#get content
	def get_content(self):
		return self.content

	def content_joiner(self):
		tools = Tools()
		text =""
		for c in self.content:
			text = text + tools.unicode_safe(c.text) + "\n"
		return text
	#length of the speak, needed for the furthur analysis
	def get_length(self):
		content_joined = self.content_joiner()
		m = re.findall('(\S+)', content_joined)
		length = 0
		if m:
			length = len(m)
		return length

#Collection for the same speaker words.
#class SpeechCollection(Speech):