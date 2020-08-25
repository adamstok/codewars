### Day2

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:

34,67,55,33,12,98

Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

```
def comma(*arr):
    listed = [str(x) for x in arr]
    return listed, tuple(listed)

list1, tuple1 = comma(1,2,3) 
```   
---


Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

```
class Mammouth():
    def getString(self):
        self.string = input('self string: ')

    def printString(self):
        print(self.string.upper())

m = Mammouth()
m.getString()
m.printString()
``` 

---

Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 * C * D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:

100,150,180
The output of the program should be:

18,22,24

```
import math
def square(*args):
    listed = [str(math.floor(math.sqrt((2 * 50 * x) / 30 ))) for x in args ]
    return ','.join(listed)

s = square(100,150,180)
``` 
---


