import random

com = random.randint(1,100)

user = int(input('Enter a number between 1 and 100:'))

while True:
    if user == com:
        print('You guessed it right')
        break
    elif user < com:
        print('Too low')
        user = int(input('Enter a number between 1 and 100:'))
    else:
        print('Too high')
        user = int(input('Enter a number between 1 and 100:'))
        