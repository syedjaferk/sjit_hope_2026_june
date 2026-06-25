
from abc import ABC, abstractmethod

class InternetService(ABC):
	@abstractmethod
	def connect_to(self):
		pass

class Internet(InternetService): # Real Object
	def connect_to(self, url):
		print("Connecting to URL - ", url)

class ProxyService(InternetService):
	def __init__(self):
		self.banned_list = ["www.thepiratebay.org"]
		self.internet = Internet() # Real Object - Aggregation

	def connect_to(self, url):
		if url in self.banned_list:
			raise Exception("can't connect to banned websites")
		else:
			return self.internet.connect_to(url)
			
object = ProxyService()
# object.connect_to("www.reddit.org")
# object.connect_to("www.thepiratebay.org")

internet = Internet()
internet.connect_to("www.thepiratebay.org")