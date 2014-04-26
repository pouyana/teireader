#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
class Tools:
    """
    **Tool**
    Tools class, tools needed in most of the code all the same
    """
    def unicode_safe(self,word):
        """
        unicode safe code (https://code.djangoproject.com/ticket/170)
        """
        if type(word) == unicode:
            word = word.encode('utf-8')
        return word

    def calc_median(self,number_list):
        """
        calculate the median number from the list of numbers
        """
        values = sorted(number_list)
        if(len(values)%2==1):
            return values[((len(values)+1)/2)-1]
        else:
            lower = values[(len(values)/2)-1]
            upper = values[(len(values)/2)]
            return (float(lower+upper))/2

    def calc_average(self,sum_of,count):
        """
        Calculates average from the sum and numbers count
        return None if division to 0
        """
        average = 0
        if((count)!= 0):
            average =  float(sum_of)/count
            return average
        else:
            return None

    def calc_sum(self,array_of_numbers):
        """
        Calculates the sum of numbers in a list
        returns 0 if list is empty or none exists.
        """
        sum_of = 0
        for i in array_of_numbers:
            sum_of = sum_of + i
        return sum_of

    def normalize_text(self,text):
        """
        Remove unintended empty strings
        """
        text = text.rstrip().lstrip()
        words = re.findall("\S+",text)
        normalized =  " ".join(words)
        return self.unicode_safe(normalized.rstrip())
