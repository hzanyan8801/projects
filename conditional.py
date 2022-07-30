def clinic():
    print ("You've just entered the clinic!")
    print ("Do you take the door on the left or the right?")
    answer = input("Type left or right and hit 'Enter'.".lower())
    if answer == "left" or answer =="l":
        print ("This is the verbal abuse room!")
    elif answer =="right" or answer =="r":
        print ("Of course this is the Argument Room")
    else:
        print ("You didn't pick left or right! Try again.")
        clinic()

clinic()