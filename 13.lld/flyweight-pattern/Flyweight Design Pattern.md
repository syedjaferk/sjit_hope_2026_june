

### When to Use ?
- When memory is limited
- When objects share the data
	- intrinsic data: shared among objects and remain same once defined one value.
	- extrinsic data: changes based on client input and differes from one object to another.
- creation of object is expensive.
- The goal of the flyweight pattern is to reduce memory usage by sharing as much data as possible, hence, it’s a good basis for lossless compression algorithms. In this case, each flyweight object acts as a pointer with its extrinsic state being the context-dependent information.


### When not to use ?

### What it is ?
Flyweight pattern is primarily used to reduce the number of objects created and to decrease memory footprint and increase performance. This type of design pattern comes under structural pattern as this pattern provides ways to decrease object count thus improving the object structure of application.

Many modern applications use caches to improve response time. The flyweight pattern is similar to the core concept of a cache and can fit this purpose well.

Of course, there are a few key differences in complexity and implementation between this pattern and a typical, general-purpose cache.

### checklist
1. Ensure that object overhead is an issue needing attention, and, the client of the class is able and willing to absorb responsibility realignment.
2. Divide the target class's state into: shareable (intrinsic) state, and non-shareable (extrinsic) state.
3. Remove the non-shareable state from the class attributes, and add it the calling argument list of affected methods.
4. Create a Factory that can cache and reuse existing class instances.
5. The client must use the Factory instead of the new operator to request objects.
6. The client (or a third party) must look-up or compute the non-shareable state, and supply that state to class methods.
7. 
### Structure

1. **Flyweight Factory :** manages a pool of existing flyweights.
2. The **Flyweight** class contains the portion of the original object’s state that can be shared between multiple objects. The same flyweight object can be used in many different contexts. The state stored inside a flyweight is called _intrinsic._ The state passed to the flyweight’s methods is called _extrinsic._
3. The **Context** class contains the extrinsic state, unique across all original objects. When a context is paired with one of the flyweight objects, it represents the full state of the original object.

![[Pasted image 20240125081716.png]]

### Example 
1. A classic example of this usage is in a word processor. Here, each character is a flyweight object which shares the data needed for the rendering. As a result, only the position of the character inside the document takes up additional memory.
2. In graphical user interface (GUI) systems, graphical elements like icons, buttons, and characters can be implemented using the **Flyweight** pattern. Common properties such as image data or icon representations are shared among multiple instances, while the position and user-specific properties are maintained separately.
3. In game development, the **Flyweight** pattern can be applied to manage game entities, such as bullets, particles, or textures. Common properties like the image or behavior are shared among instances, while the position, velocity, and other state information are specific to each instance.

### Solution
How to solve:
1. From object remove all the extrinsic data and keep intrinsic data - this is called flyweight object 
2. This flyweight class can be immutable
3. extrinsic data can be passed to the flyweight class in method parameter. 
4. Once the flyweight object is created it is cached and reused whenever required. 

### Implementation

1. Font

```python
class Font:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color

class FontFactory:
    _fonts = {}

    def get_font(self, name, size, color):
        key = (name, size, color)
        if key not in self._fonts:
            self._fonts[key] = Font(name, size, color)
        return self._fonts[key]

class Text:
    def __init__(self, content, font):
        self.content = content
        self.font = font

# Example use cases:

font_factory = FontFactory()

# Use case 1
font1 = font_factory.get_font("Arial", 12, "Black")
text1 = Text("Hello, world!", font1)

# Use case 2
font2 = font_factory.get_font("Arial", 12, "Black")
text2 = Text("Flyweight pattern example", font2)

# Use case 3
font3 = font_factory.get_font("Times New Roman", 14, "Red")
text3 = Text("Design patterns are awesome", font3)

# Use case 4
font4 = font_factory.get_font("Arial", 12, "Black")
text4 = Text("Reuse fonts for memory efficiency", font4)

# Use case 5
font5 = font_factory.get_font("Times New Roman", 14, "Red")
text5 = Text("Minimize memory usage with flyweight", font5)

```

### Advantages
1. ****Memory Efficiency:**** The Flyweight design pattern reduces the memory usage by allowing related objects to share the common state.
2. ****Performance Improvement:**** The Flyweight design pattern improves the performance in terms of processing speed and initialization time.
3. ****Resource utilization:**** The Flyweight design pattern allows efficient use of resources by minimizing the number of instances required to represent a similar object.
4. ****Reduced Redundancy:**** The Flyweight design pattern helps to reduce the redundant code by extracting the common state.
5. Encapsulation of Extrinsic State: The client maintains the extrinsic state, not within the flyweight objects. This separation allows for more straightforward management of the client’s context-specific information without affecting the shared intrinsic state.
6. 

### Disadvantages
1. ****Dependency on a Factory:**** The Flyweight design pattern often relies on a factory for creating flyweight objects, introducing a dependency on this factory.
2. ****Increased Complexity:**** Implementing the Flyweight design pattern can introduce additional complexity to the codebase, especially if the logic for managing shared and unique states is intricate.
3. If not implemented carefully, the **Flyweight** pattern may introduce thread safety concerns. If multiple threads concurrently access and modify shared flyweights, synchronization mechanisms might be needed to avoid race conditions.
4. Since flyweights represent a shared state, their changes may affect the identity of multiple objects. This can have unintended consequences and requires careful consideration, especially when dealing with mutable shared state.





[[Composite]] [[Facade]] [[Singleton Design Pattern]] 