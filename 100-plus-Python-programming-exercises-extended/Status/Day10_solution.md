Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

Hints:
Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.

```
def squaredvalues():
    print({x:x**2 for x in range(1,21)})
```

---

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

Hints:
Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

```
def generateddict():
    generated = {x:x**2 for x in range(1,21)}
    print(generated.keys())
    
```
---

Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

Hints:
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.

```
def generatedlist():
    generated = [x**2 for x in range(1,21)]
    print(generated)
```
---

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

Hints:
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list

```
def generatedlist():
    generated = [x**2 for x in range(1,21)]
    print(generated[:5])
```

---

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

Hints:
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list

```
def generatedlist():
    generated = [x**2 for x in range(1,21)]
    print(generated[-5:])
```

---

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

Hints: Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list

```
def generatedlist():
    generated = [x**2 for x in range(1,21)]
    print(generated[5:])
```

---


