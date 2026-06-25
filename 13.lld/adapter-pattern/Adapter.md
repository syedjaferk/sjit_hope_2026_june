
### When to Use ?
- Use the Adapter class when you want to use some existing class, but its interface isn’t compatible with the rest of your code.
- we can make these legacy components work seamlessly with new systems, without having to modify the existing codebase.

### What it is ?

Adapter design pattern is one of the **structural design pattern** and its used so that two unrelated interfaces can work together. The object that joins these unrelated interface is called an **Adapter**.

### Structure

### Example 
a) **Database Adapters:** When working with different database systems, each may have its own specific API. An adapter can be used to convert the operations and queries from one database system to another, allowing the client code to work with a common interface.

b) **Legacy System Integration:** When integrating new software components with existing legacy systems, the Adapter pattern can be used to translate the legacy system’s interface into a more modern and compatible one.

c) **Plug Adapters:** In electrical systems, different countries may have different types of electrical outlets. Plug adapters allow devices with one type of plug to be used with different outlet types by adapting the plug to fit the specific outlet.

- **File Format Adapters:** An application that can read data from different file formats (e.g., CSV, XML, JSON). Each file format may have its own parsing interface. To maintain a consistent interface for reading data, adapters can be used to wrap the different parsing classes and provide a unified interface for this application.


### Solution

Consider a weather application which consumes XML data, 

```python
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

```

Consider, a new JSON data provider is coming, how to use it, 

**Object based adapter**

```python
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

```

**Class based adapter**

```python
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

```

### Implementation

### Advantages
- _Single Responsibility Principle_. You can separate the interface or data conversion code from the primary business logic of the program.
- _Open/Closed Principle_. You can introduce new types of adapters into the program without breaking the existing client code, as long as they work with the adapters through the client interface.
- **Unit Testing and Mocking:** Adapters can be beneficial for unit testing and mocking. Mock implementations of interfaces that allow client code testing independent of the actual **Adaptee**‘s implementation can be created by introducing adapters.

### Disadvantages
- The overall complexity of the code increases because you need to introduce a set of new interfaces and classes.
- Can introduce additional complexity if not used judiciously.
- Increases the number of classes and complexity in the codebase.


[[Bridge Design Pattern]] [[Decorator Pattern]] [[Proxy Pattern]] [[Facade]] 
[[State Pattern]] [[Strategy Pattern]]