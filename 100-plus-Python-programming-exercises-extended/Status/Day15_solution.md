Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com
Then, the output of the program should be:

google
In case of input data being supplied to the question, it should be assumed to be a console input.

```
def getcompany():
    print(input('email: ').split('@')[1].split('.')[0])
```

---

Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

Example: If the following words is given as input to the program:

2 cats and 3 dogs.
Then, the output of the program should be:

['2', '3']
In case of input data being supplied to the question, it should be assumed to be a console input.

Hints
Use re.findall() to find all substring using regex.

```
def finddigits():
    sentence = input().split()
    print(list(filter(lambda x: x.isdigit() == True, sentence)))
```
---

Print a unicode string "hello world".

Hints
Use u'strings' format to define unicode string.

```
print(u'Hello World')
```

---

Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

Hints
Use unicode()/encode() function to convert.

```
def decodeascii(string):
    print(string.encode('utf-8'))
```

---

Write a special comment to indicate a Python source code file is in unicode.

Hints
Use unicode() function to convert.

```

# -*- coding: utf-8 -*-
```

---

Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example: If the following n is given as input to the program:

5
Then, the output of the program should be:

3.55
In case of input data being supplied to the question, it should be assumed to be a console input.

Hints
Use float() to convert an integer to a float.Even if not converted it wont cause a problem because python by default understands the data type of a value

```
def computen():
    n = int(input())
    print(f"{sum([float(x/(x+1)) for x in range(1,n+1)]):.2f}")
```
