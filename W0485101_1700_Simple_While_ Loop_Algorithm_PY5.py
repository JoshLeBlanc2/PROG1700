import datetime

x = 0 #Current Year
y = 0 #Age input
Y = 0 #Age input made into an int
z = 0 #Date of birth
#Number of times the program will loop
mainloop = 3
loop_counter = 0

while loop_counter < mainloop:

    """Main program start"""
  
    y = input("Enter your age (Must be a number):")
   
    x = datetime.datetime.now().year

    Y = int(y)

    z = x - Y

    if Y >= 1:
        print("You were born in", z)
   
    else:
            print("Error, this is an invalid answer. Your answer can ONLY include numbers above 0")

    """Main program end"""   
    loop_counter = loop_counter + 1
    print(loop_counter)

else:
    print("You have only",loop_counter,"attemps")

