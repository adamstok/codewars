import sys

for i in range(1,len(sys.argv)):
    if int(sys.argv[i]) % 3 == 0 and int(sys.argv[i]) % 5 == 0 :
        print('fizzbuzz')
    if int(sys.argv[i]) % 3 == 0 and int(sys.argv[i]) % 5 != 0 :
        print('fizz')
    if int(sys.argv[i]) % 5 == 0 and int(sys.argv[i]) % 3 != 0 :
        print('buzz')
    if int(sys.argv[i]) % 5 != 0 and int(sys.argv[i]) % 3 != 0 :
        print(f'{sys.argv[i]}')

