import random
rand=random.randint(1,10)
n=int(input('Guess the number: '))
while n != rand:
    print('Wrong, try again!')
    n=int(input('Guess the number: '))
    
print('Correct!')
