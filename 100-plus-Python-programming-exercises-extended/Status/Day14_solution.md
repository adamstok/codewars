
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

---

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com
Then, the output of the program should be:

john
In case of input data being supplied to the question, it should be assumed to be a console input.

Hints
Use \w to match letters.

```
def getusername(email):
    print(email.split('@')[0])
``` 

---
