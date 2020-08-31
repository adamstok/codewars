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

---

A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:

2

```
import math
def moved():
    x,y = 0,0
    movements = input().split()
    for i in range(len(movements)-1):
        if movements[i] == "UP":
            y += int(movements[i+1])
        if movements[i] == "DOWN":
            y -= int(movements[i+1])
        if movements[i] == "LEFT":
            x -= int(movements[i+1])
        if movements[i] == "RIGHT":
            x += int(movements[i+1])
    print(round(math.sqrt(x**2 + y**2 )))

```
