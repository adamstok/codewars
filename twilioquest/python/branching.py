import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

if num1 + num2 <= 0:
    print('You have chosen the path of destitution.')

if num1 + num2 >= 1 and num1 + num2 <= 100:
    print('You have chosen the path of plenty.')

if num1 + num2 > 100:
    print('You have chosen the path of excess.')
