Please write assert statements to verify that every number in the list [2,4,6,8] is even.

Hints
Use "assert expression" to make assertion.

```
assert list(filter(lambda x:x%2==0,[2,4,6,8])) == [2,4,6,8]
```
---

Please write a program which accepts basic mathematic expression from console and print the evaluation result.

Example: If the following n is given as input to the program:

35 + 3
Then, the output of the program should be:

38
Hints
Use eval() to evaluate an expression.

```
evaluation = print(eval(input()))
```

---

Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

Hints
Use if/elif to deal with conditions.

```
import bisect
def binary_search(element,l):
    sorted_list = sorted(l)
    index = bisect.bisect_left(sorted_list,element)
    if index < len(sorted_list) and sorted_list[index] == element:
        return index
```
