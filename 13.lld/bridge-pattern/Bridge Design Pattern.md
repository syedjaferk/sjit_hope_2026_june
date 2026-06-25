
Note:
Abstraction - Doesn't mean abstract class. Its a high-level control layer for some entity.
Implementation - Should do all the delegated work from the abstraction.

For example, Consider a GUI application (calculator) where you see a screen. There are functionalities lies behind this screen, impelmentation of the calculator.

### When to Use ?
- Use the Bridge pattern when you want to divide and organize a monolithic class that has several variants of some functionality (for example, if the class can work with various database servers).
- Use the pattern when you need to extend a class in several orthogonal (independent) dimensions.
- Use the Bridge if you need to be able to switch implementations at runtime.
- you want run-time binding of the implementation
- You have many classes because the interface is tightly connected to multiple implementations.
- **Platform-Dependent Code**: When dealing with platform-specific code, such as code that interacts with different operating systems or hardware. The Bridge pattern can help manage these differences by encapsulating platform-specific code within implementations.
- **Testing and Debugging**: When we want to improve testing and debugging by isolating the components we are testing from their implementations. This can make it easier to pinpoint issues.
- **Parallel Development**: When we are working with teams that can work on the abstraction and implementation independently. The Bridge pattern allows parallel development without tight coupling.
- **Scalability**: When we are building a system that needs to scale and evolve over time. The Bridge pattern’s separation of concerns can make it easier to handle changes and growth.

### Checklist
1. Check if two different aspects are present in the field. These could be: main idea/system, or main area/framework, or front part/back part, or how it looks/how it works.
2. Plan how to separate the important things: what the customer wants and what the systems offer.
3. Create a basic connection that focuses on the system. It should be small, necessary, and complete. The aim is to detach the main idea from the system.
4. Make a new class based on that connection for each system.
5. Develop the main idea base class that "has" a system object and assigns the system-related tasks to it.
6. Make specific versions of the main idea class if needed.

### What it is ?

As per GoF, **Bridge pattern decouples an abstraction from its implementation so that the two can vary independently.** 

So what it does is, we will separate the implementation(calculator functionality) part of the application (Calculator Screen) to a separate interface, so that they can vary independantly. 

### Structure

1. **Abstraction :** It provides high-level control logic. It relies on the implementation object to do the actual low-level work.
2. The **Implementation** declares the interface that’s common for all concrete implementations. An abstraction can only communicate with an implementation object via methods that are declared here. The abstraction may list the same methods as the implementation, but usually the abstraction declares some complex behaviors that rely on a wide variety of primitive operations declared by the implementation.
3. **Concrete Implementation**: Contain platform specific code.
4. **Refined Abstraction:** It provide variants of control logic. Like their parent, they work with different implementations via the general implementation interface.

![[Pasted image 20240120171908.png]]

### Example 

1. **Graphics Libraries**: Graphics libraries often use the Bridge pattern to separate the drawing primitives (**Abstraction**) from the specific rendering engines (**Implementation**). This allows the library to support multiple platforms or devices without changing the drawing code.
2. **Notification Systems**: Notification systems that deliver messages through different channels (email, SMS, push notifications) use the Bridge pattern. The **Abstraction** represents the notification message, while **Implementations** handle the delivery mechanisms.
3. **Vehicle Manufacturing Systems**: In the context of vehicle manufacturing, the Bridge pattern can be used to separate the types of vehicles (**Abstraction**) from their propulsion systems (**Implementation**), allowing for a variety of vehicle types with different engines.

### Examples and Implementation

1. Consider an animals that "move" in different ways. 
	1. Person that moves by walking 
	2. Fish that moves by swimming
	3. Bird that moves by flying
![[Pasted image 20240120174244.png]]
**Abstraction:** It is only obvious that there is a pattern here. Three objects that `move` but in different ways.
![[Pasted image 20240120174447.png]]

As shown in the diagram, the class Animal is an abstraction (or interface) such that the three animals inherit from it. Each animal individually implements their own specific logic as to how they `move()`. Therefore, they declare their own move method.  
However, we are still not quite there yet. Bridge pattern is **NOT** about a simple inheritance. The pattern’s intent is to **separate** the `move()`logic from the abstraction. In this example, the code within the Animal classes should only be about defining the animal object representations.

**Implementation:** Each `move()`method has a different logic (or control logic, or business logic). For example, a person walks by using his legs one at a time, a bird needs to flap its wings in a specific frequency and so on.

![[Pasted image 20240120175030.png]]

```python
from abc import ABC, abstractmethod

# Abstraction 
class Animals(ABC):
    def __init__(self, move_logic):
        self.move_logic = move_logic

    @abstractmethod
    def move(self):
        pass

# Implementation - Move
class Move(ABC):
    
    @abstractmethod
    def move(self):
        pass

# Concrete Implementation
class Walk(Move):

    def move(self):
        print("Movement is walking")

# Concrete Implementation
class Fly(Move):

    def move(self):
        print("Movement is flying")

# Concrete Implementation
class Swim(Move):

    def move(self):
        print("Movement is Swiming")

# Concrete Abstraction
class Person(Animals):

    def __init__(self, move_logic: Move):
        self.move_logic = move_logic
    
    def move(self):
        self.move_logic.move()

# Concrete Abstraction
class Bird(Animals):

    def __init__(self, move_logic: Move):
        self.move_logic = move_logic
    
    def move(self):
        self.move_logic.move()

# Concrete Abstraction
class Fish(Animals):

    def __init__(self, move_logic: Move):
        self.move_logic = move_logic
    
    def move(self):
        self.move_logic.move()

def client_code():
    gold_fish = Fish(move_logic=Swim())
    gold_fish.move()

client_code()
```

2. Consider an application that allows us to download and store files on any operating systems. 
- We want to design the system in such a way, we should be able to add more platform support in the future with minimum change.
- Additionally, If I want to add more support in the downloader class (e.g. delete the download in Windows only), then It should not affect the client code as well as the Linux downloader.

```python
from abc import ABC, abstractmethod

# Abstraction
class FileDownloader(ABC):

    def __init__(self, file_func_provider):
        self.file_func_provider = file_func_provider

    @abstractmethod
    def store(self):
        pass

    @abstractmethod
    def download(self):
        pass

# Implementor
class FileFuncProvider(ABC):

    @abstractmethod
    def store(self):
        pass

    @abstractmethod
    def download(self):
        pass

# Concrete Implementor Class
class LinuxFileFuncProvider(FileFuncProvider):

    def store(self):
        print("File stored in linux")
    
    def download(self):
        print("File downloaded in Linux")

# Concrete Implementor Class
class WindowsFileFuncProvider(FileFuncProvider):

    def store(self):
        print("File stored in windows")
    
    def download(self):
        print("File downloaded in windows")


# Abstraction Implmentation Class
class FileDownloaderImplementation(FileDownloader):

    def __init__(self, file_func_provider: FileFuncProvider):
        self.file_func_provider = file_func_provider

    def store(self):
        self.file_func_provider.store()

    def download(self):
        self.file_func_provider.download()

os_name = "windows"

if os_name == "windows":
    obj = FileDownloaderImplementation(file_func_provider=WindowsFileFuncProvider())
elif os_name == "linux":
    obj = FileDownloaderImplementation(file_func_provider=LinuxFileFuncProvider())
else:
    raise Exception("OS Not available")

obj.store()
obj.download()

```

if now we add 'delete' method inside FileFuncProvider it wont affect the FileDownloader class. viceversa. 

3. Fileoperations on different storage type.
**Without Bridge pattern:**
```python
class FileManager:
    def __init__(self, storage_type):
        self.storage_type = storage_type

    def read_file(self, filename):
        if self.storage_type == "Local":
            return f"Reading {filename} from local storage"
        elif self.storage_type == "Cloud":
            return f"Reading {filename} from cloud storage"

# Problem: Adding a new storage type requires modifying the FileManager class.

```

**With Bridge Pattern**
```python
class FileManager:
    def __init__(self, storage):
        self.storage = storage

    def read_file(self, filename):
        return self.storage.read(filename)

class Storage:
    def read(self, filename):
        pass

class LocalStorage(Storage):
    def read(self, filename):
        return f"Reading {filename} from local storage"

class CloudStorage(Storage):
    def read(self, filename):
        return f"Reading {filename} from cloud storage"

# Now, adding a new storage type is easy by extending the Storage class.

```

4. Notifying users through different channels
**Without Bridge pattern**
```python
class NotificationService:
    def __init__(self, channel):
        self.channel = channel

    def send_notification(self, message):
        if self.channel == "Email":
            return f"Sending email notification: {message}"
        elif self.channel == "SMS":
            return f"Sending SMS notification: {message}"

# Problem: Adding a new notification channel requires modifying the NotificationService class.

```

**With Bridge Pattern**

```python
class NotificationService:
    def __init__(self, channel):
        self.channel = channel

    def send_notification(self, message):
        return self.channel.send(message)

class NotificationChannel:
    def send(self, message):
        pass

class EmailChannel(NotificationChannel):
    def send(self, message):
        return f"Sending email notification: {message}"

class SMSChannel(NotificationChannel):
    def send(self, message):
        return f"Sending SMS notification: {message}"

# Now, adding a new notification channel is easy by extending the NotificationChannel class.

```

5. working with various database servers
**Without Bridge Pattern**
```python
class MonolithicDatabaseHandler:
    def __init__(self, database_type):
        self.database_type = database_type

    def connect(self, credentials):
        if self.database_type == "mongodb":
            print("Connecting to MongoDB with credentials:", credentials)
        elif self.database_type == "mysql":
            print("Connecting to MySQL with credentials:", credentials)
        else:
            raise ValueError("Unsupported database type")

    def execute_query(self, query):
        if self.database_type == "mongodb":
            print("Executing MongoDB query:", query)
        elif self.database_type == "mysql":
            print("Executing MySQL query:", query)
        else:
            raise ValueError("Unsupported database type")

    def fetch_results(self):
        if self.database_type == "mongodb":
            print("Fetching MongoDB results")
        elif self.database_type == "mysql":
            print("Fetching MySQL results")
        else:
            raise ValueError("Unsupported database type")

# Client code:
def main():
    mongodb_handler = MonolithicDatabaseHandler("mongodb")
    mongodb_handler.connect({"host": "localhost", "port": 27017})
    mongodb_handler.execute_query({"find": "users"})
    mongodb_handler.fetch_results()

    mysql_handler = MonolithicDatabaseHandler("mysql")
    mysql_handler.connect({"host": "mysql.example.com", "user": "root", "password": "secret"})
    mysql_handler.execute_query("SELECT * FROM customers")
    mysql_handler.fetch_results()

if __name__ == "__main__":
    main()

```

**With Bridge Pattern**

```python
from abc import ABC, abstractmethod

# Abstraction: Database Handler
class DatabaseHandler(ABC):
    def __init__(self, implementation):
        self.implementation = implementation

    @abstractmethod
    def connect(self, credentials):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass

    @abstractmethod
    def fetch_results(self):
        pass

class DBImplementor(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self):
        pass

    @abstractmethod
    def fetch_results(self):
        pass

# Implementation: MongoDB Implementation
class MongoDB(DBImplementor):
    def connect(self, credentials):
        print("Connecting to MongoDB with credentials:", credentials)

    def execute_query(self, query):
        print("Executing MongoDB query:", query)

    def fetch_results(self):
        print("Fetching MongoDB results")

# Implementation: MySQL Implementation
class MySQL(DBImplementor):
    def connect(self, credentials):
        print("Connecting to MySQL with credentials:", credentials)

    def execute_query(self, query):
        print("Executing MySQL query:", query)

    def fetch_results(self):
        print("Fetching MySQL results")

# Client code:
def main():
    mongodb_handler = MongoDB()
    mongodb_handler.connect({"host": "localhost", "port": 27017})
    mongodb_handler.execute_query({"find": "users"})
    mongodb_handler.fetch_results()

    mysql_handler = MySQL()
    mysql_handler.connect({"host": "mysql.example.com", "user": "root", "password": "secret"})
    mysql_handler.execute_query("SELECT * FROM customers")
    mysql_handler.fetch_results()

if __name__ == "__main__":
    main()

```
### Advantages
- You can create platform-independent classes and apps.
- The client code works with high-level abstractions. It isn’t exposed to the platform details.
- _Open/Closed Principle_. You can introduce new abstractions and implementations independently from each other.
- _Single Responsibility Principle_. You can focus on high-level logic in the abstraction and on platform details in the implementation.
- 

### Disadvantages
- You might make the code more complicated by applying the pattern to a highly cohesive class.
- **Potential Over-Abstraction**: In some cases, designers might overuse the pattern, creating unnecessary layers of abstraction that complicate the system without providing tangible benefits.

[[Decorator Pattern]] [[Adapter]] [[Bridge Design Pattern]] [[State Pattern]] [[Strategy Pattern]] [[Builder Design Pattern]]
