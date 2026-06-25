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

class JSONDataProviderInterface(ABC):

    @abstractmethod
    def read_json_data(self):
        pass

    @abstractmethod
    def get_value_from_json(self):
        pass

class JSONDataProvider(JSONDataProviderInterface):

    def __init__(self):
        self.data = None

    def read_json_data(self):
        with open("data.json", encoding="utf-8") as file:
            data = json.load(file)
        self.data = data
    
    def get_value_from_json(self, key):
        return self.data.get(key)

class JSONtoXMLAdapter(DataProviderInterface):

    def __init__(self, json_provider: JSONDataProvider):
        self.json_provider = json_provider
    
    def collect_data(self):
        self.json_provider.read_json_data()
    
    def get_value(self, key):
        return self.json_provider.get_value_from_json(key)


class Weather():
    def __init__(self, data_provider: XMLDataProvider):
        self.data_provider = data_provider
        self.data_provider.collect_data()
    
    def print_weather(self):
        res = f"At {self.data_provider.get_value('time')} temperature is {self.data_provider.get_value('temp')} {self.data_provider.get_value('unit')}"
        print(res)

# def client_code():
#     xml_data_provider = XMLDataProvider()
#     weather = Weather(data_provider=xml_data_provider)
#     weather.print_weather()

def client_code():
    json_provider = JSONDataProvider()
    xml_json_adapter = JSONtoXMLAdapter(json_provider)
    weather = Weather(data_provider=xml_json_adapter)
    weather.print_weather()

if __name__=='__main__':
    client_code()
