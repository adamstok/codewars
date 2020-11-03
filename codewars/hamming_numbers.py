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


@runtime
def hamming(n):
    outp = [0, 1]
    count_i = 0
    count_j = 0
    count_k = 0
    if n == 1:
        return 1
    while True:
        for i in range(2, n**n):
            if len(outp) > n:
                return outp[n]
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                pass
            else:
                if i % 2 == 0:
                    count_i += 1
                    a = i // 2
                    while type(a) == int:
                        if a % 2 == 0:
                            a = a // 2
                            count_i += 1
                        else:
                            a = a / 2
                if i % 3 == 0:
                    count_j += 1
                    b = i // 3
                    while type(b) == int:
                        if b % 3 == 0:
                            b = b // 3
                            count_j += 1
                        else:
                            b = b / 3
                if i % 5 == 0:
                    count_k += 1
                    c = i // 5
                    while type(c) == int:
                        if c % 5 == 0:
                            c = c // 5
                            count_k += 1
                        else:
                            c = c / 5
                if 2**count_i * 3**count_j * 5**count_k == i:
                    outp.append(i)
                    count_i = 0
                    count_j = 0
                    count_k = 0
                else:
                    count_i = 0
                    count_j = 0
                    count_k = 0


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
