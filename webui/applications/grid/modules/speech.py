#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import re for the regex
import re
from tools import Tools
import math
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
		text =" "
		for c in self.content:
                        if (c.text):
			    text = text + tools.unicode_safe(c.text) + "\n"
		return text
	
	#length of the speak, needed for the furthur analysis
	def get_length(self):
		m = self.get_words_array()
                length = 0
		if m:
			length = len(m)
		return length
	#have the word array for each speech
	def get_words_array(self):
		content_joined = self.content_joiner()
		m = re.findall('(\S+)', content_joined)
		return m
		
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
		tools = Tools()
		self.average = tools.calc_average(self.get_sum(),self.get_count())
	
	#sorted length useful 
	def get_sorted_length(self):
		return sorted(self.get_speech_length())

	#set the median for the length
	def set_median(self):
		tools = Tools()
		values = self.get_speech_length()
		self.median = tools.calc_median(values)
class WordPack():
	'''Packs of speech diffrent length from the orignial'''
	def __init__(self,speaker,words):
		self.speaker = speaker
		self.speech = words
	def get_speaker(self):
		return self.speaker
	def get_speech(self):
		return self.speech
	def get_speech_length(self):
		return len(self.speech)
	def pop_element(self):
		speech = self.speech
		a = speech.pop()
		self.speech = speech
		return a

class WordPackCollection():
	'''a Collection of 500 packs of words, disregarding their speaker'''
	def __init__(self):
		self.wordpack_list = []
		self.word_count = 0
		self.speaker_dict =[]
		self.statis_dict = []
	#get the speaker average speech length in the pack
	def speaker_numbers(self):
		speaker_dict = []
		for wordpack in self.wordpack_list:
			speaker = next((item for item in speaker_dict if item["speaker"] == wordpack.get_speaker()), None)
			if (speaker==None):
				spk = {}
				numbers = []
				numbers.append(wordpack.get_speech_length())
				spk["speaker"] = wordpack.speaker
				speaker2 = next((item for item in self.statis_dict if item["speaker"] == wordpack.get_speaker()), None)
				if(speaker2 == None):
					self.statis_dict.append(spk)
				spk["numbers"] = numbers
				speaker_dict.append(spk)	
			else:
				speaker["numbers"].append(wordpack.get_speech_length())
		self.speaker_dict = speaker_dict

	def speaker_average(self):
		tools = Tools()
		for spk in self.speaker_dict:
			average = tools.calc_average(tools.calc_sum(spk["numbers"]),len(spk["numbers"]))
			speaker = next((item for item in self.statis_dict if item["speaker"] == spk["speaker"]), None)
			if(speaker !=None):
				if("average" not in speaker):
					speaker["average"]=[]
					speaker["average"].append(average)
				else:
					speaker["average"].append(average)

	def speaker_median(self):
		tools = Tools()
		for spk in self.speaker_dict:
			median = tools.calc_median(spk["numbers"])
                        speaker = next((item for item in self.statis_dict if item["speaker"] == spk["speaker"]), None)
			if(speaker !=None):
	                        if("median" not in speaker):
        	                        speaker["median"]=[]
                	                speaker["median"].append(median)
                        	else:
                                	speaker["median"].append(median)

	#the array of the median
	def get_statis_dict(self):
		return self.statis_dict
	
	#add speech to the wordpack list
	def add_speech(self,speech):
		speech_container = []
		for word in speech.get_words_array():
			if (self.word_count != 500):
				self.word_count = self.word_count + 1
				speech_container.append(word)
			else:
				self.speaker_numbers()
				self.speaker_average()
				self.speaker_median()
				self.del_words()
		if(len(speech_container)>0):
			if "." in speech.get_speaker():
				speaker = speech.get_speaker()
			else:
                                speaker = speech.get_speaker() + "."
			wordpack = WordPack(speaker, speech_container)
			self.wordpack_list.append(wordpack)

	#delete the first 10 element of the 500 pack
	#we move the pointer	
	def del_words(self):
		#with 10 and 10 range you are to slow for testing use 1000 (with 500 spans)
		self.word_count = self.word_count-50
		for i in range(0,50):
			if(len(self.wordpack_list)>0):
				wordpack = self.wordpack_list[0]
				if(not wordpack.get_speech()):
					self.wordpack_list.pop(0)
					if (len(self.wordpack_list) > 0):
						wordpack = self.wordpack_list[0]
						wordpack.pop_element()
				else:
					wordpack.pop_element()
	#caluclate cumulative average
	def cul_average(self):
		tools = Tools()
		cul_average = []
		for statis in self.get_statis_dict():
			sta = {}
			sta["speaker"] = statis["speaker"]
			sta["average"] = tools.calc_average(tools.calc_sum(statis["average"]),len(statis["average"]))
			cul_average.append(sta)
		return cul_average

	#calculate cumulatice median
	def cul_median(self):
		tools = Tools()
		cul_median = []
		for statis in self.get_statis_dict():
			sta = {}
			sta["speaker"] = statis["speaker"]
			sta["median"] = tools.calc_median(statis["median"])
			cul_median.append(sta)
		return cul_median

class SpeakerStatisticsCollection():
	'''a Collection of Statistics, get a list of speech elements and creates some SpeakerStatistics from them'''
	def __init__(self,speech_list):
		self.speech_list = speech_list
		self.statistics = {}
		self.counts = []
		self.median_count = 0
		self.average_count = 0
		self.wordpack_statis = []
	def get_speech_list(self):
		return self.speech_list
		
	#a statistics object extra for the whole text.
	def generate_stats(self):
		word_count = 0
		wordpacks = WordPackCollection()
		pause = False
		spkwhole = SpeakerStatistics("whole")
		self.statistics["whole"]=spkwhole
		for spc in self.get_speech_list():
			self.statistics["whole"].add_speech(spc.get_length())
			if "." in spc.get_speaker():
				speaker = spc.get_speaker()
			else:
				speaker = spc.get_speaker() + "."
			if(speaker not in self.statistics):
				spkstat = SpeakerStatistics(speaker)
				spkstat.add_speech(spc.get_length())
				wordpacks.add_speech(spc)
				self.statistics[speaker] = spkstat
			else:
				spkstat = self.statistics[speaker]
				spkstat.add_speech(spc.get_length())
				wordpacks.add_speech(spc)
		for key,value in self.statistics.items():
			if(key!="whole"):
				self.counts.append(value.get_count())
		tools = Tools()
		self.median_count = tools.calc_median(self.counts)
		self.average_count = tools.calc_average(tools.calc_sum(self.counts),len(self.counts))
		self.wordpack_statis = wordpacks.get_statis_dict()
		self.wordpack_median = wordpacks.cul_median()
		self.wordpack_average = wordpacks.cul_average()
	def get_median_count(self):
		return self.median_count
	def get_average_count(self):
		return self.average_count
	def get_statistics(self):
		return self.statistics
	def get_wordpack_statis(self):
		return self.wordpack_statis
	def get_wordpack_median(self):
		return self.wordpack_median
	def get_wordpack_average(self):
		return self.wordpack_average
