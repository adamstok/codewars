# Define a function that takes in two non-negative integers a and b and returns the last decimal digit of a^b. Note that a and b may be very large!

# For example, the last decimal digit of 9^7 is 9, since 9^7 = 4782969. The last decimal digit of (2^200)^(2^300), which has over 10^92 decimal digits, is 6. Also, please take 0^0 to be 1.

# You may assume that the input will always be valid.

# Examples
# last_digit(4, 1)                # returns 4
# last_digit(4, 2)                # returns 6
# last_digit(9, 7)                # returns 9
# last_digit(10, 10 ** 10)        # returns 0
# last_digit(2 ** 200, 2 ** 300)  # returns 6

def last_digit(n1,n2):
    return int(str(n1**n2)[-1])

# TODO: timeout with big numbers !


assert last_digit(4, 1) ==  4
assert last_digit(4, 2) ==  6
assert last_digit(9, 7) ==  9
assert last_digit(10, 10 ** 10) ==  0
assert last_digit(2 ** 200, 2 ** 300) ==  6
assert last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651) ==  7

