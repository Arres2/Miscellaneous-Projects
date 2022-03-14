welcome = print("You're in car driving to see your girlfriend. She's home alone so you better hurry. Write 'help' to see the commands you need to get to her")
commands = ""
movement = True
while commands != "quit":
    commands = input(">").lower()
    if commands == "help":
        print("'Start' to start the car")
        print("'Stop' to stop the car")
        print("'Quit' to exit game")
    elif commands == "start":
        print("The car has started. Drive towards your girl dude")
        if movement:
            print ("You are moving towards your goal")
        else:
            movement = False
            print ("You are not moving")
        commands = input(f"You have arrived to your first intersection, what will you do? Turn right or left? R/L ")
        if commands =="R".lower():
            print ("You got stuck in traffic, what a bummer... You lose")
            commands = "quit"
        else:
            print("There´s no traffic, that´s good! Keep going-")
            while commands != "quit":
                commands = input("You reached a stop sign, what will you do?  ")
                if commands == "Stop".lower():
                    stopped_by_cops = False
                    movement = False
                    print("The car has stopped. You can check for other cars. A cop car goes by")
                    while commands != "quit":
                        commands = input("Keep going? Y/N ")
                        if commands == "Y".lower():
                            movement = True
                            print("You kept going and passed the stop sign")
                            while commands != "quit":
                                commands = input("Wich road will you take: Highway or roads? H/R ")
                                if commands == "H".lower():
                                    print ("There is no traffic but be careful not to crash")
                                    while commands != "quit":
                                        print("You got there in time, you win! Have fun ;)")
                                        commands = "quit"
                                else:
                                    if stopped_by_cops:
                                        print ("You took too long to get there... you lose")
                                        commands = "quit"
                                    else:
                                        print("It will take a little longer but you'll get there")
                                        while commands != "quit":
                                            print ("You got there in time, you win! Have fun ;)")
                                            commands = "quit"
                        else:
                            print("You are wasting time!")
                else:
                    print("You got pulled over by the cops and got a ticket you shithead, you lost a lot of time")
                    stopped_by_cops = True
                    while commands != "quit":
                        commands = input("Keep going? Y/N ")
                        if commands == "Y".lower():
                            movement = True
                            print("You kept going and passed the stop sign")
                            while commands != "quit":
                                commands = input("Wich road will you take: Highway or roads? H/R ")
                                if commands == "H".lower():
                                    print ("There is no traffic but be careful not to crash")
                                    while commands != "quit":
                                        print("You got there in time, you win! Have fun ;)")
                                        commands = "quit"
                                else:
                                    if stopped_by_cops:
                                        print ("You took too long to get there... you lose")
                                        commands = "quit"
                                    else:
                                        print("It will take a little longer but you'll get there")
                                        while commands != "quit":
                                            print ("You got there in time, you win! Have fun ;)")
                                            commands = "quit"
                        else:
                            print("You are wasting time!")
    elif commands == "quit":
        print("Good bye")
    else:
        print("Sorry I don´t understand that")

