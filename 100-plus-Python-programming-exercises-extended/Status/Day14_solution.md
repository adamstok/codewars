
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
