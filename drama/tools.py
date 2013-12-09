#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Tools:
	"""Tools class, tools needed in most of the code all the same"""

	#unicode safe code (https://code.djangoproject.com/ticket/170)
	def unicode_safe(self,word):
		if type(word) == unicode:
			word = word.encode('utf-8')
		return word
