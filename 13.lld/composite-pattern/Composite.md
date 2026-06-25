https://miro.com/app/board/uXjVN5kDS9I=/

### When to Use ?
- When we you have to implement a tree-like object structure.
- When we want the client code to treat both simple and complex elements uniformly.
### When not to use ?
1. **Different Stuff:** If the things in your system (like unable to group objects together) are very different from each other, the Composite Pattern might not be the best fit. It works better when everything follows a similar pattern.
2.  **Speed Issues:** If your system needs to be super fast, the Composite Pattern could slow it down because of how it organizes things. In really speedy situations, simpler ways might be better.
3. **Always Changing:** If your system keeps changing a lot, especially with things being added or taken away frequently, using the Composite Pattern might not be the easiest or most efficient way.
4. **Not Too Complicated:** If your system isn't very complicated and doesn't have a lot of layers or levels, using the Composite Pattern might make things more complex than they need to be.
5. **No Clear Hierarchy:** If your system doesn't have a clear order or structure, or if most things are just by themselves without being part of a bigger group, the Composite Pattern might be too much.
6. **Can't Change How Things Work:** If you can't change how the different things in your system work together, the Composite Pattern might not fit well because it likes things to have a common way of doing stuff.
7. **Worried About Memory:** If your system needs to use as little memory as possible, the Composite Pattern might use more than you'd like. In memory-sensitive situations, it might be better to use simpler methods.

### What it is ?
**Composite** is a structural design pattern that lets you compose objects into tree structures and then work with these structures as if they were individual objects.

As described by Gof, “Compose objects into tree structure to represent ****part-whole hierarchies****. Composite lets client treat individual objects and compositions of objects uniformly”.

### Structure

1. **Component**: The **Component** interface describes operations that are common to both simple and complex elements of the tree.
2. **Leaf**: The **Leaf** is a basic element of a tree that doesn’t have sub-elements.   Usually, leaf components end up doing most of the real work, since they don’t have anyone to delegate the work to.
3. **Composite**: The **Container** (aka _composite_) is an element that has sub-elements: leaves or other containers. A container doesn’t know the concrete classes of its children. It works with all sub-elements only via the component interface.
4. **Client:** The **Client** works with all elements through the component interface. As a result, the client can work in the same way with both simple or complex elements of the tree.

![[composite_design_pattern.jpg]]

## Check list

1. Ensure that your problem is about representing "whole-part" hierarchical relationships.
2. Consider the heuristic, "Containers that contain containees, each of which could be a container." For example, "Assemblies that contain components, each of which could be an assembly." Divide your domain concepts into container classes, and containee classes.
3. Create a "lowest common denominator" interface that makes your containers and containees interchangeable. It should specify the behavior that needs to be exercised uniformly across all containee and container objects.
4. All container and containee classes declare an "is a" relationship to the interface.
5. All container classes declare a one-to-many "has a" relationship to the interface.
6. Container classes leverage polymorphism to delegate to their containee objects.
7. Child management methods [e.g. `addChild()`, `removeChild()`] should normally be defined in the Composite class. Unfortunately, the desire to treat Leaf and Composite objects uniformly may require that these methods be promoted to the abstract Component class. See the Gang of Four for a discussion of these "safety" versus "transparency" trade-offs.

### Example 
1. Let’s suppose we are building a financial application. We have customers with multiple bank accounts. We are asked to prepare a design which can be useful to generate the customer’s consolidated account view which is able to show **customer’s total account balance as well as consolidated account statement** after merging all the account statements. So, application should be able to generate:

1) Customer’s total account balance from all accounts  
2) Consolidated account statement
![[Pasted image 20240119230015.png]]
```python
from abc import ABC, abstractmethod

# Component
class AccountComponent(ABC):
    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def get_statement(self):
        pass

# Leaf
class BankAccount(AccountComponent):
    def __init__(self, account_number, balance, statement):
        self.account_number = account_number
        self.balance = balance
        self.statement = statement

    def get_balance(self):
        return self.balance

    def get_statement(self):
        return f"Account {self.account_number} Statement:\n{self.statement}"

# Composite
class CustomerAccount(AccountComponent):
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_balance(self):
        total_balance = sum(account.get_balance() for account in self.accounts)
        return total_balance

    def get_statement(self):
        consolidated_statement = f"Consolidated Statement for {self.customer_name}:\n"
        for account in self.accounts:
            consolidated_statement += account.get_statement() + "\n"
        return consolidated_statement

# Usage
if __name__ == "__main__":
    account1 = BankAccount("123456", 5000, "Transaction 1: +$100\nTransaction 2: -$50")
    account2 = BankAccount("789012", 7000, "Transaction 1: +$200\nTransaction 2: -$100")

    customer = CustomerAccount("John Doe")
    customer.add_account(account1)
    customer.add_account(account2)

    # Generate Customer’s total account balance
    total_balance = customer.get_balance()
    print(f"Customer's Total Account Balance: ${total_balance}")

    # Generate Consolidated account statement
    consolidated_statement = customer.get_statement()
    print(consolidated_statement)

```

1. Let’s consider a car. Car has an engine and a tire. The engine is made up of some electrical components and valves. 
![[Pasted image 20240119230157.png]]
```python
 from abc import ABC, abstractmethod

 # Component (Leaf)
 class Component(ABC):
     @abstractmethod
     def get_price(self):
         pass

 # Leaf
 class Transistor(Component):
     def get_price(self):
         return 10 

 # Leaf
 class Chip(Component):
     def get_price(self):
         return 20  

 # Leaf
 class Valve(Component):
     def get_price(self):
         return 15  

 # Leaf
 class Tire(Component):
     def get_price(self):
         return 50  

 # Composite
 class Composite(Component):
     def __init__(self, name):
         self.name = name
         self.components = []

     def add_component(self, component):
         self.components.append(component)

     def get_price(self):
         total_price = sum(component.get_price() for component in self.components)
         return total_price

 # Client code
 if __name__ == "__main__":
     # Creating leaf objects
     transistor = Transistor()
     chip = Chip()
     valve = Valve()
     tire = Tire()

     # Creating composite objects
     electrical_components = Composite("Electrical Components")
     electrical_components.add_component(transistor)
     electrical_components.add_component(chip)
     electrical_components.add_component(valve)

     engine = Composite("Engine")
     engine.add_component(electrical_components)

     car = Composite("Car")
     car.add_component(engine)
     car.add_component(tire)

     # Applying operation on leaf objects
     print(f"Transistor Price: {transistor.get_price()}")
     print(f"Chip Price: {chip.get_price()}")
     print(f"Valve Price: {valve.get_price()}")
     print(f"Tire Price: {tire.get_price()}")

     # Applying operation on composite objects
     print(f"Engine Price: {engine.get_price()}")
     print(f"Car Price: {car.get_price()}")

```
### Implementation

#### 1. Graphic Shapes in a Drawing Application:
```python
from abc import ABC, abstractmethod

# Component
class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass

# Leaf
class Circle(Graphic):
    def draw(self):
        print("Drawing Circle")

# Leaf
class Square(Graphic):
    def draw(self):
        print("Drawing Square")

# Composite
class CompositeGraphic(Graphic):
    def __init__(self):
        self.graphics = []

    def add(self, graphic):
        self.graphics.append(graphic)

    def draw(self):
        print("Drawing Composite:")
        for graphic in self.graphics:
            graphic.draw()

# Usage
circle = Circle()
square = Square()
composite = CompositeGraphic()
composite.add(circle)
composite.add(square)

composite.draw()

```

2. File System Representation:

```python
from abc import ABC, abstractmethod

# Component
class FileSystemComponent(ABC):
    @abstractmethod
    def size(self):
        pass

# Leaf
class File(FileSystemComponent):
    def __init__(self, size):
        self.size_value = size

    def size(self):
        return self.size_value

# Composite
class Directory(FileSystemComponent):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def size(self):
        # Component
        class FileSystemComponent(ABC):
            @abstractmethod
            def size(self):
                pass
        
        # Leaf
        class File(FileSystemComponent):
            def __init__(self, size):
                self.size_value = size

        total_size = sum(child.size() for child in self.children)
        return total_size

# Usage
file1 = File(10)
file2 = File(5)
directory = Directory()
directory.add(file1)
directory.add(file2)

print("Total Size:", directory.size())

```

3. Organization Hierarchy
```python
from abc import ABC, abstractmethod

# Component
class Employee(ABC):
    @abstractmethod
    def show_details(self):
        pass

# Leaf
class IndividualEmployee(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def show_details(self):
        print(f"{self.position}: {self.name}")

# Composite
class Manager(Employee):
    def __init__(self, name):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)

    def show_details(self):
        print(f"Manager: {self.name}")
        for subordinate in self.subordinates:
            subordinate.show_details()

# Usage
individual1 = IndividualEmployee("John", "Developer")
individual2 = IndividualEmployee("Alice", "Tester")
manager = Manager("Bob")
manager.add_subordinate(individual1)
manager.add_subordinate(individual2)

manager.show_details()

```

4. Menu Hierarchy in Restaurant
```python
from abc import ABC, abstractmethod

# Component
class MenuItem(ABC):
    @abstractmethod
    def display(self):
        pass

# Leaf
class Dish(MenuItem):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name} - ${self.price}")

# Composite
class Menu(MenuItem):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display(self):
        print("Menu:")
        for item in self.items:
            item.display()

# Usage
dish1 = Dish("Spaghetti", 12.99)
dish2 = Dish("Salad", 7.99)
menu = Menu()
menu.add_item(dish1)
menu.add_item(dish2)

menu.display()

```

5. Tree structure of Document Elements:
```python
from abc import ABC, abstractmethod

# Component
class MenuItem(ABC):
    @abstractmethod
    def display(self):
        pass

# Leaf
class Dish(MenuItem):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name} - ${self.price}")

# Composite
class Menu(MenuItem):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display(self):
        print("Menu:")
        for item in self.items:
            item.display()

# Usage
dish1 = Dish("Spaghetti", 12.99)
dish2 = Dish("Salad", 7.99)
menu = Menu()
menu.add_item(dish1)
menu.add_item(dish2)

menu.display()

```


### Advantages
- You can work with complex tree structures more conveniently: use polymorphism and recursion to your advantage.
- _Open/Closed Principle_. You can introduce new element types into the app without breaking the existing code, which now works with the object tree.
- Uniform treatment of leaf and composite objects.
- Its particularly useful when dealing with hierarchial structures.
- Scalability - we can easily new types of components to the entire hierarchy.
- encapsulation

### Disadvantages

- It might be difficult to provide a common interface for classes whose functionality differs too much. In certain scenarios, you’d need to over generalize the component interface, making it harder to comprehend.
- If individual **leaf** objects have unique properties or behaviors, the **Composite** pattern may not be the best choice, as it enforces a uniform interface across all components. In such cases, you may need to resort to other patterns or adaptations.
- Storing hierarchy objects can consume memory if its deep. 
- 

## Relation
Builder Chain Of Responsibility Iterators Visitor Flyweights [[Decorator Pattern]]
[[Builder Design Pattern]] [[Flyweight Design Pattern]] [[Iterator Design Pattern]] [[Visitor Design Pattern]] [[Prototype Design Pattern]]
