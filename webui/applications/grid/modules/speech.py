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

	#get the id
	def get_id(self):
		return self.id

	#set the content of the speech
	def set_content(self,content):
		self.content = content

	#get content
	def get_content(self):
		return self.content

	#generate a string from the array given
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

class SpeakerStatistics:
	'''Statistics for the speaker words. Here the median and average are calculated'''
	def __init__(self,speaker):
		self.set_speaker(speaker)
		self.speech_length=[]
		self.sum = 0
	
	def __str__(self):
		return "Speaker: " + str(self.speaker) + " has median speech of " + str(self.get_median()) + " and the average of " + str(self.get_average())

	def add_speech(self,length):
		self.add_sum(length)
		self.add_to_speech_length(length)

	#add to the sum
	def add_sum(self,length):
		self.sum = self.sum + length
	
	#sum of the whole words speaker speaking
	def get_sum(self):
		return self.sum
	
	def set_count(self):
		self.count = len(self.speech_length)
	#how many speeches for a speaker (realtime)
	def get_count(self):
		self.set_count()
		return self.count
	
	#get/set speaker
	def get_speaker(self):
		return self.speaker
	def set_speaker(self,speaker):
		self.speaker = speaker
	
	#get/set speech length array
	def get_speech_length(self):
		return self.speech_length
	def set_speech_length(self,lengths):
		self.speech_length = lengths
	
	#add new items to the speech length array
	def add_to_speech_length(self,length):
		self.speech_length.append(length)
	
	#get median from speech length (Repliklänge)
	def get_median(self):
		self.set_median()
		return self.median

	#get average length:
	def get_average(self):
		self.set_average()
		return self.average

	#set the average
	def set_average(self):
		#no divide / 0
		self.average = 0
		if(self.get_count() != 0):
			self.average =  self.get_sum()/self.get_count()
	
	#sorted length useful 
	def get_sorted_length(self):
		return sorted(self.get_speech_length())

	def set_median(self):
		values = self.get_sorted_length()
		if(len(values)%2==1):
			#odd number of elements
			self.median = values[((len(values)+1)/2)-1]
		else:
			#even number
			lower = values[(len(values)/2)-1]
			upper = values[(len(values)/2)]
			self.median = (float(lower+upper))/2

class SpeakerStatisticsCollection():
	'''a Collection of Statistics, get a list of speech elements and creates some SpeakerStatistics from them'''
	def __init__(self,speech_list):
		self.speech_list = speech_list
		self.statistics = {}
	
	def get_speech_list(self):
		return self.speech_list

	def generate_stats(self):
		#a statistics object extra for the whole text.
		spkwhole = SpeakerStatistics("whole")
		self.statistics["whole"]=spkwhole
		for spc in self.get_speech_list():
			self.statistics["whole"].add_speech(spc.get_length())
			#check if the speakers all have the dot so we don't get the same speaker doubled.
			if "." in spc.get_speaker():
				speaker = spc.get_speaker()
			else:
				speaker = spc.get_speaker() + "."

			if(speaker not in self.statistics):
				spkstat = SpeakerStatistics(speaker)
				spkstat.add_speech(spc.get_length())
				self.statistics[speaker] = spkstat
			else:
				spkstat = self.statistics[speaker]
				spkstat.add_speech(spc.get_length())

	def get_statistics(self):
		return self.statistics