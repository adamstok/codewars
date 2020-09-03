Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

Hints:
Use map() to generate a list. Use lambda to define anonymous functions.

```
result = list(map(lambda x:x**2, range(1,21)))

```
---

Define a class named American which has a static method called printNationality.

Hints:
Use @staticmethod decorator to define class static method.There are also two more methods.To know more, go to this link.
```
class American:
    @staticmethod
    def printNationality():
        print('American')

```
---

Define a class named American and its subclass NewYorker.

Hints:
Use class Subclass(ParentClass) to define a subclass.*

```
class American:
    def __init__(self):
        self.nationality = 'American'

class NewYorker(Amercian):
    def __init__(self):
        self.city = 'NY'
        super().__init__()
```
