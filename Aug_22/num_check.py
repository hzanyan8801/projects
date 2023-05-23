


def user_choice():
    # Variables

    #Initial
    choice = 'WRONG'
    acceptable_range = range(0,10)
    within_range = False

    #Two conditions to check
    #Digit or Within_range==False
    while choice.isdigit() == False or within_range == False:
        
        choice = input("Please enter a number 0-10: ")

        #Digit check
        if choice.isdigit == False:
            print("Sorry that is not a digit!")

        #Range check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range == True
            else: 
                print("Sorry, you are out of acceptable range (0-10")
                within_range == False
    return int(choice)

print(user_choice())

