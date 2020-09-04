Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

Hints
Use def methodName(self) to define a method.

```
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)
```
---

Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

Hints
Use def methodName(self) to define a method.

```
class Rectangle:
    def __init__(self, l, w):
        self.lenght = l
        self.width = w
    def area(self):
        return self.length * self.width
```
---

Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints
To override a method in super class, we can define a method with the same name in the super class.

```
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,l):
        super().__init__()
        self.length = l
    def area(self):
        return self.length ** 2

```
