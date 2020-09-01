Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:

2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
Hints
In case of input data being supplied to the question, it should be assumed to be a console input.

```
def frequency():
    outp = ''
    sentence = input().split()
    keys = sorted({x for x in sentence})
    values = {x:sentence.count(x) for x in keys}
    for i in values.items():
        outp += str(i[0]) + ':' + str(i[1]) + ' '
    return outp[:-1]
    
```
---


Write a method which can calculate square value of number

Hints:
Using the ** operator which can be written as n**p where means n^p

```
def squared(number):
    return number ** 2
```

---


Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

And add document for your own function

Hints:
The built-in document method is __doc__


