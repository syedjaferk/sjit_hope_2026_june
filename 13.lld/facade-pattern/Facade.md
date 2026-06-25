
### When to Use ?
- when you need to have a limited but straightforward interface to a complex subsystem.
- Use the Facade when you want to structure a subsystem into layers.
- Facade define an entry point to each subsystem level. 
- Use the Facade pattern to promote loose coupling between Clients and Subsystem components.
- Use the Facade pattern when we want to improve the ease of use for clients.
- While integrating with the legacy side.

### When not to use ?

- If your system is small and has a straightforward structure with minimal interactions between its components, introducing a facade might add unnecessary complexity.
- If the complexity of your subsystem is not causing issues for clients, and clients are already able to use the subsystem components directly without much trouble, a facade might be unnecessary.
- Applying the Facade Pattern when it's not needed can be considered over-engineering.

### What it is ?

**Facade** is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes.

A facade is a class that provides a simple interface to a complex subsystem which contains lots of moving parts. A facade might provide limited functionality in comparison to working with the subsystem directly.

### How it's coming in to picture ?

The Facade Pattern comes into play when you have a complex system with many components, each having its own interfaces and functionality. The purpose of the Facade Pattern is to provide a simplified and unified interface to this set of interfaces, making it easier for clients to interact with the subsystem.

### Structure
1. **Client :** Client uses the facade instead of subsystem objects.
2. **Facade :** It provides convenient access to a particular part of the subsystem’s functionality. It knows where to direct the client’s request and how to operate all the moving parts.
3. **Additional Facade** : It can be created to prevent polluting a single facade with unrelated features that might make it yet another complex structure. Additional facades can be used by both clients and other facades.
4. **Subsystem Classes :** The **Complex Subsystem** consists of dozens of various objects. To make them all do something meaningful, you have to dive deep into the subsystem’s implementation details, such as initializing objects in the correct order and supplying them with data in the proper format.

![[Pasted image 20240121190037.png]]

### Example 
1. Consider a HomeTheater Facade,
```python
# Subsystem classes
class Amplifier:
    def turn_on(self):
        print("Amplifier turned on")

    def turn_off(self):
        print("Amplifier turned off")


class DVDPlayer:
    def play_movie(self, movie):
        print(f"Playing movie: {movie}")

    def stop_movie(self):
        print("Stopping movie")


class Projector:
    def turn_on(self):
        print("Projector turned on")

    def turn_off(self):
        print("Projector turned off")


class Lights:
    def dim_lights(self):
        print("Dimming lights")

    def brighten_lights(self):
        print("Brightening lights")


# Facade class
class HomeTheaterFacade:
    def __init__(self, amplifier, dvd_player, projector, lights):
        self.amplifier = amplifier
        self.dvd_player = dvd_player
        self.projector = projector
        self.lights = lights

    def watch_movie(self, movie):
        print("Get ready to watch a movie!")
        self.lights.dim_lights()
        self.amplifier.turn_on()
        self.projector.turn_on()
        self.dvd_player.play_movie(movie)

    def end_movie(self):
        print("Movie night is over!")
        self.dvd_player.stop_movie()
        self.amplifier.turn_off()
        self.projector.turn_off()
        self.lights.brighten_lights()


# Client code
amplifier = Amplifier()
dvd_player = DVDPlayer()
projector = Projector()
lights = Lights()

home_theater = HomeTheaterFacade(amplifier, dvd_player, projector, lights)

# Watching a movie using the Facade
home_theater.watch_movie("Inception")

# Ending the movie night
home_theater.end_movie()

```

2. Computer Sytems
```python
class CPU:
    def process_data(self):
        print("Processing data")


class Memory:
    def load_data(self):
        print("Loading data into memory")


class HardDrive:
    def read_data(self):
        print("Reading data from hard drive")


class ComputerFacade:
    def __init__(self, cpu, memory, hard_drive):
        self.cpu = cpu
        self.memory = memory
        self.hard_drive = hard_drive

    def start(self):
        self.cpu.process_data()
        self.memory.load_data()
        self.hard_drive.read_data()


# Client code
cpu = CPU()
memory = Memory()
hard_drive = HardDrive()

computer_facade = ComputerFacade(cpu, memory, hard_drive)
computer_facade.start()

```
3. Online shopping system
```python
class Inventory:
    def check_availability(self, item):
        print(f"Checking availability of {item}")

class PaymentGateway:
    def process_payment(self, amount):
        print(f"Processing payment of {amount}")

class Shipping:
    def ship_item(self, item):
        print(f"Shipping {item}")

class ShoppingFacade:
    def __init__(self, inventory, payment_gateway, shipping):
        self.inventory = inventory
        self.payment_gateway = payment_gateway
        self.shipping = shipping

    def purchase_item(self, item, amount):
        self.inventory.check_availability(item)
        self.payment_gateway.process_payment(amount)
        self.shipping.ship_item(item)

# Client code
inventory = Inventory()
payment_gateway = PaymentGateway()
shipping = Shipping()

shopping_facade = ShoppingFacade(inventory, payment_gateway, shipping)
shopping_facade.purchase_item("Laptop", 1000)

```

### Advantages
- You can isolate your code from the complexity of a subsystem
- 

### Disadvantages
- A facade can become [a god object](https://refactoring.guru/antipatterns/god-object) coupled to all classes of an app.

[[Adapter]] [[Flyweight Design Pattern]] [[Mediator Design Pattern]] [[Abstract Factory Pattern]]
