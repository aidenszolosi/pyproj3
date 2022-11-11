#we must import a library, "random"

import random 

while True:
    while True:
        maxValue = input('\nWhat should the highest number for this game be? ')
        if maxValue.isdigit():
            maxValue = int(maxValue)
            RandomNumber = (random.randint(1, maxValue))
            guess = input("Make a guess! What's the number? ")
            guess = int(guess)
            if guess == RandomNumber:
                print('WINNER!!!')
            else:
                print('Try again')
                print('The number was ' + str(RandomNumber))
                break
        
        else:
            print('WTF IDIOT THATS NOT A NUMBER')
         