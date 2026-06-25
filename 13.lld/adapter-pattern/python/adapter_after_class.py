"""
Adapter class with class based implementation
"""
import json
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup


class DataProviderInterface(ABC):
    """
    DataProvider Interface
    Methods:
        collect_data: to collect the data
        get_value: to get the value from data
    """

    def __init__(self):
        self.data = None

    @abstractmethod
    def collect_data(self):
        """
        Method to collect the data
        """
        pass

    @abstractmethod
    def get_value(self, key):
        """
        Method to get value from data
        """
        pass


class XMLDataProvider(DataProviderInterface):
    """
    DataProvider: XML Data Provider
    """
    def __init__(self):
        """
        Initialization of the attr.
        """
        self.data = None

    def collect_data(self):
        with open("data.xml", encoding="utf-8") as file:
            data = file.read()
        print("test")
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

class JSONtoXMLAdapter(JSONDataProvider, XMLDataProvider):
    
    def collect_data(self):
        self.json_data_provider = JSONDataProvider()
        self.json_data_provider.read_json_data() 
    
    def get_value(self, key):
        return self.json_data_provider.get_value_from_json(key)


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
    xml_json_adapter = JSONtoXMLAdapter()
    weather = Weather(data_provider=xml_json_adapter)
    weather.print_weather()

if __name__=='__main__':
    client_code()
