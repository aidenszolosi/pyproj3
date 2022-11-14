#aiden szolosi
#started on 11/10/22

#we must import a library, "random"

#Receive input from the user
#Output data to the console
##XApply conditional logic
##XConvert string value to int
##X - Use the Random library
#Use while loops
import random 

while True:
    maxValue = input('\nWhat should the highest number for this game be? ')
    if maxValue.isdigit():
        maxValue = int(maxValue)
        RandomNumber = int((random.randint(1, maxValue)))
        while True:
            guess = input("Make a guess! What's the number? ")
            guess = int(guess)
            if guess == RandomNumber:
                print("You got it!, It was " + str(RandomNumber))  
                break   
            elif guess <= RandomNumber:
                print('\tHigher!')
            elif guess >= RandomNumber:
                print('\tLower!')
    else: 
        print('That does not seem to be a valid response?')


###print('The number was ' + str(RandomNumber)) 