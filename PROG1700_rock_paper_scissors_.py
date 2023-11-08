#Comments

#Import modules here
import random

#Global variables
invalid_attemps = 3

#Program control
while True:
    #Local Variable user_input
    user_input = input("Type 1 for rock, 2 for paper, 3 for sicssors:")
    #Validate the input to ensure the program does not have an invalid input
    # Return true is a digit is entered, otherwise return false
    if user_input.isdigit():
        
        if len(user_input) == 1: 
            #Cast to an integer
            user_input = int(user_input)
            # 1, 2, 3 numbers only
            #Calculate the bot's value
            bot_value = random.randrange(1,3)
            # Print the bots answer
            print(bot_value)
               
            if user_input == bot_value:
                print("Tie, try again")
            else:
                if user_input == 1 and bot_value == 3:
                    print("User Wins")
                else:
                    if user_input == 2 and bot_value == 1:
                        print("User Wins")
                    else:
                        if user_input == 3 and bot_value == 2:
                            print("User Wins")
                        else:
                            print("Bot Wins")
                           
