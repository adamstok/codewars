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
