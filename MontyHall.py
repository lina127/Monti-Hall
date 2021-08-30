import random

mode= int (input("Which mode do you wanna play? (1 or 2): "))

if mode == 1:
    door = [ 1, 2, 3 ]
    porche = door [random.randint(0,2)]
    print (porche)
    yourguess = input("Pick a door between 1 to 3: ")
    print ("You have chosen door #", yourguess)
    print ("We will open a door that 지노니 is behind.")

    flag = False
    openDoor = door[random.randint(0,2)]
    while flag == False:
        if int(openDoor) == int(porche) or int(openDoor) == int(yourguess):
            openDoor = door[random.randint(0,2)]
        else:
            print ("지노니 is at door #", openDoor)
            flag = True

    switch = input("Do you want to switch door? (y/Y or n/N): ")
    if switch.upper() == "Y":
        sumup = int(yourguess) + int(openDoor)
        leftDoor = int(6- sumup)
        if leftDoor == int(porche):
            print ("Congratulation!")
        else:
            print ("Loser")
            
    elif switch.upper() == "N":
        if int(yourguess) == int(porche):
            print ("Congratulation")
        else:
            print ("Loser")
            
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
        
