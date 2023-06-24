import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWQYZ123456789!@#$%^&*()~"

while 1:
    try:
        Password_Len = int(input("What length would you like your password to be : "))
        Password_count = int(input("How many passwords would you like to have generated? :"))
    except ValueError:
        print("Invalid Entry")
    else:
     for x in range(0,Password_count):
            Password = ""
            for x in range (0,Password_Len):
                Password_characters = random.choice(characters)
                Password = Password + Password_characters
            print("Here is your Password :", Password)

    break
    
