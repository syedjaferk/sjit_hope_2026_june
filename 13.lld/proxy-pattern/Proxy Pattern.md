Board Link: https://miro.com/app/board/uXjVN5kDS9I=/

### Also Known As
- Surrogate
- Placeholder
### When to Use ?
 - **Lazy initialization (virtual proxy).** This is when you have a heavyweight service object that wastes system resources by being always up, even though you only need it from time to time. Instead of creating the object when the app launches, you can delay the object’s initialization to a time when it’s really needed.
 
- **Access Control**: This is when you want only specific clients to be able to use the service object; for instance, when your objects are crucial parts of an operating system and clients are various launched applications (including malicious ones). The proxy can pass the request to the service object only if the client’s credentials match some criteria 

- **Remote proxy**: Local execution of a remote service (remote proxy). This is when the service object is located on a remote server. In this case, the proxy passes the client request over the network, handling all of the nasty details of working with the network.

- **Logging proxy**: This is when you want to keep a history of requests to the service object.

- **Caching proxy**: Caching request results (caching proxy). This is when you need to cache results of client requests and manage the life cycle of this cache, especially if results are quite large.

- **Smart reference.** This is when you need to be able to dismiss a heavyweight object once there are no clients that use it.
### When not to use ?

- During minimal behaviour extension. 
- If its adding performance overhead due to delegation of function calls.

### What it is ?

**Proxy** is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

It also helps in caching the resource, so that new same objects aren't created again.

### How it's coming in to picture ?
### Structure

1. **Service Interface** :  (Concrete Interface) Declares the interface of the service. The proxy must follow this interface to be able to accommodate the service objects. 
2. **Service**: (Concrete Class) A class that provides some business logic.
3. **Proxy Class**: Implements service interface, also has a reference field to a service object. After the proxy finishes its processing (e.g., lazy initialization, logging, access control, caching, etc.), it passes the request to the service object. Usually, proxies manage the full lifecycle of their service objects.
4. **Client**: The **Client** should work with both services and proxies via the same interface. This way you can pass a proxy into any code that expects a service object.
![[Pasted image 20231228111239.png]]



### Example 

1. A bank's cheque or credit card is a proxy for what is in our bank account. It can be used in place of cash, and provides a means of accessing that cash when required. And that’s exactly what the Proxy pattern does – “Controls and manage access to the object they are protecting“.

2. A company or corporate used to have a proxy which restricts few site access. The proxy first checks the host you are connecting to, if it is not a part of restricted site list, then it connects to the real internet.


### Solution

1. **Bank Example:** 
![[Pasted image 20231228124032.png]]

2. Internet 

```python

from abc import ABC, abstractmethod

class InternetService(ABC):
	@abstractmethod
	def connect_to(self):
		pass

class Internet(InternetService):
	def connect_to(self, url):
		print("Connecting to URL - ", url)

class ProxyService(InternetService):
	def __init__(self):
		self.banned_list = ["www.thepiratebay.org"]
		self.internet = Internet()

	def connect_to(self, url):
		if url in self.banned_list:
			raise Exception("can't connect to banned websites")
		else:
			return self.internet.connect_to(url)
			
```


### Implementation

#### Virtual Proxy
```python
class RealObject:
    def perform_action(self):
        print("RealObject performing action")

class Proxy:
    def __init__(self):
        self._real_object = None

    def perform_action(self):
        if self._real_object is None:
            self._real_object = RealObject()
        self._real_object.perform_action()

# Client code
proxy = Proxy()
proxy.perform_action()

```


#### Remote Proxy

```python
from abc import ABC, abstractmethod

class RemoteObject(ABC):
    @abstractmethod
    def perform_action(self):
        pass

class RealRemoteObject(RemoteObject):
    def perform_action(self):
        print("RealRemoteObject performing action")

class RemoteProxy(RemoteObject):
    def __init__(self):
        self._real_object = None

    def perform_action(self):
        if self._real_object is None:
            self._real_object = RealRemoteObject()
        self._real_object.perform_action()

# Client code
proxy = RemoteProxy()
proxy.perform_action()

```

#### Protection proxy

```python
class RealObject:
    def perform_action(self):
        print("RealObject performing action")

class Proxy:
    def __init__(self, user):
        self._real_object = RealObject()
        self._user = user

    def perform_action(self):
        if self._user == "admin":
            self._real_object.perform_action()
        else:
            print("Access denied for non-admin user")

# Client code
admin_proxy = Proxy("admin")
admin_proxy.perform_action()

user_proxy = Proxy("user")
user_proxy.perform_action()

```

#### Logging Proxy

```python
from abc import ABC, abstractmethod

# Interface for the Calculator service
class CalculatorService(ABC):
    @abstractmethod
    def add(self, x, y):
        pass

    @abstractmethod
    def subtract(self, x, y):
        pass

# Real implementation of the Calculator service
class Calculator(CalculatorService):
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

# Logging Proxy for the Calculator service
class LoggingProxy(CalculatorService):
    def __init__(self, real_calculator):
        self._real_calculator = real_calculator

    def _log(self, method, *args):
        print(f"Logging: {method}({args})")

    def add(self, x, y):
        self._log("add", x, y)
        result = self._real_calculator.add(x, y)
        print(f"Result of add operation: {result}")
        return result

    def subtract(self, x, y):
        self._log("subtract", x, y)
        result = self._real_calculator.subtract(x, y)
        print(f"Result of subtract operation: {result}")
        return result

# Client code
def client_code(calculator):
    result_add = calculator.add(10, 5)
    result_subtract = calculator.subtract(20, 7)

# Using the Calculator directly
print("Using Calculator:")
real_calculator = Calculator()
client_code(real_calculator)

# Using the LoggingProxy to add logging to the Calculator
print("\nUsing LoggingProxy:")
logging_proxy = LoggingProxy(real_calculator)
client_code(logging_proxy)

```

#### Caching Proxy

```python
from abc import ABC, abstractmethod

# Interface for the Calculator service
class CalculatorService(ABC):
    @abstractmethod
    def add(self, x, y):
        pass

    @abstractmethod
    def subtract(self, x, y):
        pass

# Real implementation of the Calculator service
class Calculator(CalculatorService):
    def add(self, x, y):
        print("Performing add operation")
        return x + y

    def subtract(self, x, y):
        print("Performing subtract operation")
        return x - y

# Caching Proxy for the Calculator service
class CachingProxy(CalculatorService):
    def __init__(self, real_calculator):
        self._real_calculator = real_calculator
        self._cache = {}

    def add(self, x, y):
        key = f"add:{x}:{y}"
        if key not in self._cache:
            result = self._real_calculator.add(x, y)
            self._cache[key] = result
            print(f"Caching result for add({x}, {y}): {result}")
        else:
            print(f"Using cached result for add({x}, {y})")
        return self._cache[key]

    def subtract(self, x, y):
        key = f"subtract:{x}:{y}"
        if key not in self._cache:
            result = self._real_calculator.subtract(x, y)
            self._cache[key] = result
            print(f"Caching result for subtract({x}, {y}): {result}")
        else:
            print(f"Using cached result for subtract({x}, {y})")
        return self._cache[key]

# Client code
def client_code(calculator):
    result_add1 = calculator.add(10, 5)
    result_add2 = calculator.add(10, 5)  # This should use the cached result
    result_subtract1 = calculator.subtract(20, 7)
    result_subtract2 = calculator.subtract(20, 7)  # This should use the cached result

# Using the Calculator directly
print("Using Calculator:")
real_calculator = Calculator()
client_code(real_calculator)

# Using the CachingProxy to add caching to the Calculator
print("\nUsing CachingProxy:")
caching_proxy = CachingProxy(real_calculator)
client_code(caching_proxy)


```

### Advantages

- You can control the service object without clients knowing about it
- You can manage the lifecycle of the service object when clients don’t care about it.
- The proxy works even if the service object isn’t ready or is not available.
- [[Open Closed Principle]] You can introduce new proxies without changing the service or clients.

### Disadvantages

- The code may become more complicated since you need to introduce a lot of new classes.
- The response from the service might get delayed. Due to delegation.

### Relations

[[Adapter]] [[Decorator Pattern]] [[Facade]] [[Structural Design Patterns]] 
