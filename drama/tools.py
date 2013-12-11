#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Tools:
	"""Tools class, tools needed in most of the code all the same"""

	#unicode safe code (https://code.djangoproject.com/ticket/170)
	def unicode_safe(self,word):
		if type(word) == unicode:
			word = word.encode('utf-8')
		return word
	
	#calculate median for an array of number
	def calc_median(self,number_list):
		 values = number_list
		if(len(values)%2==1):
			#odd number of elements
			return = values[((len(values)+1)/2)-1]
		else:
			#even number
			lower = values[(len(values)/2)-1]
			upper = values[(len(values)/2)]
			return = (float(lower+upper))/2
	
	#calculate the average
	def calc_average(self,sum_of,count):
		#no divide / 0
		average = 0
		if(count)!= 0):
			average =  float(sum_of/count)
		return average

	#calculate the some of an array numbers
	def calc_sum(self,array_of_numbers):
		sum_of = 0
		for i in array_of_numbers:
			sum_of = sum_of + i
		return sum_of