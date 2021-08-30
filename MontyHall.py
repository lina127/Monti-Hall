import random

print("Welcome, there are 2 goats and 1 car behind each doors. \n It's time to win a car!") 

mode= int (input("Which mode do you wanna play? \n To see the probability, select mode 2.[1=Manual],[2=Automatic]: "))

if mode == 1:
    door = [ 1, 2, 3 ]
    porche = door [random.randint(0,2)]
    print (porche)
    yourguess = input("Pick a door between 1 to 3: ")
    print ("You have chosen door #", yourguess)
    print ("We will open a door that goat is behind.")

    flag = False
    openDoor = door[random.randint(0,2)]
    while flag == False:
        if int(openDoor) == int(porche) or int(openDoor) == int(yourguess):
            openDoor = door[random.randint(0,2)]
        else:
            print ("Goat is at door #", openDoor)
            flag = True

    switch = input("Do you want to switch door? (y/Y or n/N): ")
    if switch.upper() == "Y":
        sumup = int(yourguess) + int(openDoor)
        leftDoor = int(6- sumup)
        if leftDoor == int(porche):
            print ("Congratulation. You win the car!")
        else:
            print ("It was a goat door...")
            
    elif switch.upper() == "N":
        if int(yourguess) == int(porche):
            print ("Congratulation. You win the car!")
        else:
            print ("It was a goat door...")
            
elif mode == 2:
    rotation = int (input("How many times do you want to run?: "))
    yCounter = 0
    for i in range (rotation):
        door = [ 1, 2, 3 ]
        porche = door [random.randint(0,2)]
        yourguess = door [random.randint(0,2)]
        
        flag = False
        openDoor = door[random.randint(0,2)]
        while flag == False:
            if int(openDoor) == int(porche) or int(openDoor) == int(yourguess):
                openDoor = door[random.randint(0,2)]
            else:
                flag = True

        sumup = int(yourguess) + int(openDoor)
        leftDoor = int(6- sumup)
        if leftDoor == int(porche):
            yCounter += 1

    percentage = (float(yCounter) / float(rotation)) * 100.0
    rounding= round(percentage , 2 )
    unchange= round (100.0 - rounding , 2)


    print ("If you change the door, answer percentage is: ", str (rounding) +"%")
    print ("If you don't change, answer percentage is: ", str(unchange) +"%" )
        
