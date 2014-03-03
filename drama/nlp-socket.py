#this module is used to create socket connection to the stanford server. it is needed for the named entity recognition with higher speed.
#to start the named entity recognition server:
#java -mx1000m -cp stanford-ner-2014-01-04.jar edu.stanford.nlp.ie.NERServer -loadClassifier classifiers/hgc_175m_600.crf.ser.gz -port 9191 -outputFormat inlineXML
#to start pos_tag:
#java -mx1000m -cp stanford-postagger-3.3.1.jar edu.stanford.nlp.tagger.maxent.MaxentTaggerServer -model models/german-dewac.tagger -port 9192 -outputFormat inlineXML
import socket
class NLPSocket:
	def __init__(self,host,port):
		self.host = host
		self.port = port
		self.create_socket()
	
	def create_socket(self):
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((self.host, self.port))
		self.socket = s

	def recv_data(self,data):
		self.socket.sendall(data)
		self.socket.shutdown(socket.SHUT_WR)
		data = self.socket.recv(16384)
		self.socket.close()
		return data
#test case:
nlp = NLPSocket("localhost",9191)
data = nlp.recv_data("Mein Name ist Brad John")
print data
