import json
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

class DataProviderInterface(ABC):

    def __init__(self):
        self.data = None

    @abstractmethod
    def collect_data(self):
        pass

    @abstractmethod
    def get_value(self, key):
        pass

class XMLDataProvider(DataProviderInterface):

    def __init__(self):
        self.data = None

    def collect_data(self):
        with open("data.xml", encoding="utf-8") as file:
            data = file.read()
        bs_xml = BeautifulSoup(data, "xml")
        self.data = bs_xml
    
    def get_value(self, key):
        value = self.data.find(key)
        return value.text if value else value


class Weather():
    def __init__(self, data_provider: XMLDataProvider):
        self.data_provider = data_provider
    
    def print_weather(self):
        res = f"At {self.data_provider.get_value('time')} temperature is {self.data_provider.get_value('temp')} {self.data_provider.get_value('unit')}"
        print(res)

def client_code():
    xml_data_provider = XMLDataProvider()
    xml_data_provider.collect_data()
    weather = Weather(data_provider=xml_data_provider)
    weather.print_weather()

if __name__=='__main__':
    client_code()
