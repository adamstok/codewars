"""
A Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.

Write a function that computes the nth smallest Hamming number.

Specifically:

The first smallest Hamming number is 1 = 203050
The second smallest Hamming number is 2 = 213050
The third smallest Hamming number is 3 = 203150
The fourth smallest Hamming number is 4 = 223050
The fifth smallest Hamming number is 5 = 203051
The 20 smallest Hamming numbers are given in example test fixture.

"""
import time


def runtime(f):
    def wrap(*args):
        t1 = time.time()
        outp = f(*args)
        t2 = time.time()
        print(f'runtime: {t2-t1} sec')
        return outp
    return wrap


# def numbs(n):
#     yield n
#     yield from numbs(n+1) # => max recursion depth exceeded


def gotit(n, mod):
    count = 0
    if n % mod == 0:
        count += 1
        a = n // mod
        while type(a) == int:
            if a % mod == 0:
                a = a // mod
                count += 1
            else:
                a = a / mod
    return count


@runtime
def hamming(n):
    outp = [0, 1]
    two, three, five = 0, 0, 0
    if 1 <= n <= 2:
        return n
    for b in range(2, n**n):
        if len(outp) > n:
            print(f'{len(outp)} >= {n}')
            return outp[n]
        if b % 2 != 0 and b % 3 != 0 and b % 5 != 0:
            pass
        else:
            if b % 2 == 0:
                two = gotit(b, 2)
            if b % 3 == 0:
                three = gotit(b, 3)
            if b % 5 == 0:
                five = gotit(b, 5)
            if 2**two * 3**three * 5**five == b:
                outp.append(b)
                two, three, five = 0, 0, 0
            else:
                two, three, five = 0, 0, 0
    return outp[n]


print(hamming(500))  # 300 => runtime = 0.1004800


# assert hamming(1) == 1
# assert hamming(2) == 2
# assert hamming(3) == 3
# assert hamming(4) == 4
# assert hamming(5) == 5
# assert hamming(6) == 6
# assert hamming(7) == 8
# assert hamming(8) == 9
# assert hamming(9) == 10
# assert hamming(10) == 12
# assert hamming(11) == 15
# assert hamming(12) == 16
# assert hamming(13) == 18
# assert hamming(14) == 20
# assert hamming(15) == 24
# assert hamming(16) == 25
# assert hamming(17) == 27
# assert hamming(18) == 30
# assert hamming(19) == 32
