import random
n = random.randint(1,12)
for i in range(3):
    guess = int(input('Type an Integer(1~12):'))
    if guess == n :
        print('your guess right!')
        break
    elif guess > n :
        print('Your geuss is bigger')
    else :
        print('Your guess is smaller')
    if i == 2 : print('Sorry! No more chance!! n is ' + str(n) )
