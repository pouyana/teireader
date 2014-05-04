#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

class NLPSocket:
	"""
	Socket Library for the connection to the Stanford Servers.
	There are two servers:
	
	1. The Named Entity Recognition Server (NER):
	
	.. code-block:: java
	
		java -mx1000m -cp stanford-ner-2014-01-04.jar edu.stanford.nlp.ie.NERServer -loadClassifier classifiers/hgc_175m_600.crf.ser.gz -port 9191 -outputFormat inlineXML

	2. The Part of Speech Tagger (POSTAGGER):
	
	.. code-block:: java

		java -mx1000m -cp stanford-postagger-3.3.1.jar edu.stanford.nlp.tagger.maxent.MaxentTaggerServer -model models/german-dewac.tagger -port 9192 -outputFormat inlineXML
	
	to Test:
	
	.. code-block:: python

			nlp = NLPSocket("localhost",9191)
			data = nlp.recv_data("Mein Name ist Brad John")
			print data
	"""
	def __init__(self,host,port):
		self.host = host
		self.port = port
		self.create_socket()
	
	def create_socket(self):
		"""
		Abstract Socket creator.
		"""
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((self.host, self.port))
		self.socket = s

	def recv_data(self,data):
		"""
		Data reciver
		
		@param data, the data sent to the server

		@return string, the tagged data from one of the server.
		"""
		self.socket.sendall(data)
		self.socket.shutdown(socket.SHUT_WR)
		data = self.socket.recv(32000)
		self.socket.close()
		return data
