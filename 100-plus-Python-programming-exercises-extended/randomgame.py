import sys
import random
n1 = sys.argv[1]
n2 = sys.argv[2]
while True:
	num = int(input(f'Guess the number btw {n1}-{n2}: '))
	randomguess = random.randint(int(n1),int(n2)+1)
	if num == randomguess:
		print('You guessed it ! Congrats!')
		break
	else:
		print('Try again')
