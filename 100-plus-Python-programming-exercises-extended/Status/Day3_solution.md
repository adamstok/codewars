Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
Then, the output should be:

again and hello makes perfect practice world

```
def sortedwords():
    words = input()
    return ' '.join(sorted(set(words.split()))
```

---

Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:

0100,0011,1010,1001
Then the output should be:

1010
Notes: Assume the data is input by console.

```
def divisiblebinary():
    raw_numbers = input().split(',')
    divisible = [x for x in raw_numbers if int(x,2) % 5 == 0 ]
    print(','.join(divisible))

```


