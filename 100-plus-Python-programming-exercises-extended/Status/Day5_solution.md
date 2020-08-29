Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. Suppose the following input is supplied to the program:

1,2,3,4,5,6,7,8,9
Then, the output should be:

1,9,25,49,81

```
def squareodd():
    numbers = [int(x) for x in input().split(',')]
    return ','.join([str(x ** 2) for x in numbers if x % 2 != 0])

```
---


Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100
Then, the output should be:

500


