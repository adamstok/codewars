
Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints
Use try/except to catch exceptions.

```
def zerodivision():
    try:
        return 5/0
    except ZeroDivisionError:
        print('Zero division !')
```
---

Define a custom exception class which takes a string message as attribute.

Hints
To define a custom exception, we need to define a class inherited from Exception.

```
class CustomException(Exception):
    def __init__(self, message="Error"):
        self.message = message
        super().__init__(self.message)

```
