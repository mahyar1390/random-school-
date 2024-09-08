import random
n=randomn=random.randint(1,10)
for k in range(3):
    s=int(input('your guess:'))
    if n==s:
        print('Done!')
        break
    else:
        print('Repeat')
