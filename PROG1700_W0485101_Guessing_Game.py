#Import the random module, so that the bot can generate a random number
import random

#Global Variables
bot_number = 0
invalid_attemps = 3

loop_counter = 3
mainloop = 0
 
#Have the bot ask for your name, repeat your name and explain the game
name_input = input("Hello, what's your name?:")

#Have the bot choose a random number from 1 to 10. It's important that this line comes BEFORE the while loop, so that the bot doesn't guess a new number every try
bot_number = random.randrange(1,10)

if name_input == str(name_input):
    print("Hello", name_input, "I will guess a number from 1-10, and you'll have to try and guess the number I picked. I'll give you 3 tries to guess it")
#Set up the while loop so that they only have a limited amount of guesses
    while loop_counter > mainloop:
   
        user_input = input("Guess a number between 1-10:")
   
        if user_input.isdigit():

            if  len(user_input) == 1:

                user_input = int(user_input)
                
                if user_input > bot_number:
                    print(user_input, "Is too high")
                else:
                    if user_input < bot_number:
                        print(user_input, "Is too low")
                    else:
                        if user_input == bot_number:
                            print(user_input, "is the correct number, You win!")
                            break
        else:
            print("You cannot guess a letter")                    
        
        loop_counter = loop_counter - 1
        print("You have",loop_counter,"guesses remaining")

    else:
        print("You weren't able to guess the number, you lose. Oh, my number was", bot_number, "in case you were wondering.")

#I'm not sure how to make it so the user can only guess a number between 1-10, but i believe the rest should be good.