Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use class, function and comprehension.

```
class Q20():
    def generator(self, n):
        for i in range(n+1):
            if i % 7 == 0:
                yield i

g = Q20().generator(14)
for _ in g:
    print(_)
```
