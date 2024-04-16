# prompt user for their name and welcome user
name = input("What is your name? ")
print("Welcome " + name + "to the Adventure Game!")

# prompt user to start adventure
answer1 = input("\nYou are in a forest alone and you see a light coming from the right. "
               "Do you want to continue left or right? Type 'left' for left and 'right' for right: ").lower()

# check which option the user chose for question 1
if answer1 == "left":
    answer2 = input("You trip over a branch and fall down a steep hill. While falling, you hurt your leg "
                    "and stumble to walk. Do you continue walking or do you stop and rest? Type 'stop' to stop"
                    " and 'rest' to test: ").lower()
    # check which option the user chose for question 2
    if answer2 == "stop":
        answer3 = input("You stopped and fell asleep until you heard something approaching fast to your location. Do you stay "
              "and fight or try to get away? Type 'fight' to fight or 'away' to away")
        if answer3 == "fight":
            print("You grabbed a knife from your backpack and a bear comes out from the woods. "
                            "You kill the bear. You win :)")
        elif answer3 == "away":
            print("You stumble away the best you can, but it's no match for the bear approaching rapidly."
                  " The bear catches up and you are terminated. You lose :(")
        else:
            print("Not a valid option. You lose!")
            quit()
    elif answer2 == "rest":
        answer4 = input("You fall asleep for hours only to wake up to a strange man watching you from behind a tree. "
                        "Do you approach the man or run away? Type 'approach' to approach or 'run' to run")
        if answer4 == "approach":
            print("You approached the man and he lures you to his cabin where you are never seen or heard from again."
                  " You lose :(")
        elif answer4 == "run":
            print("You run away as best as you can, and you come out on to road with a car approaching. They stop and "
                  "take you to safety. You win :)")
        else:
            print("Not a valid option. You lose!")
            quit()
    else:
        print("Not a valid option. You lose!")
        quit()
elif answer1 == "right":
    answer5 = input("You walk towards the light and see a castle as big as a mountain. "
                    "Do you knock on the door or do sneak around? Type 'knock' to knock around and 'sneak' to sneak "
                    "around")
    if answer5 == "knock":

    elif answer5 == "sneak":

    else:
        print("Not a valid option. You lose!")
        quit()
else:
    print("Not a valid option. You lose!")
    quit()