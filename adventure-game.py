# prompt user for their name and welcome user
name = input("What is your name? ")
print("Welcome " + name + " to the Adventure Game!")

# prompt user to start adventure
answer1 = input("\nYou are in a forest alone and you see a light coming from the right. "
                "\nDo you want to continue left or right? Type 'left' for left and 'right' for right: ").lower()

# check which option the user chose for question 1
if answer1 == "left":
    answer2 = input("\nYou trip over a branch and fall down a steep hill. While falling, you hurt your leg "
                    "and stumble to walk. \nDo you continue walking or do you stop and rest? Type 'stop' to stop"
                    " and 'rest' to test: ").lower()
    # check which option the user chose for question 2
    if answer2 == "stop":
        answer3 = input("\nYou stopped and fell asleep until you heard something approaching fast to your location."
                        "\nDo you stay and fight or try to get away? Type 'fight' to fight or 'away' to away: ").lower()
        if answer3 == "fight":
            print("\nYou grabbed a knife from your backpack and a bear comes out from the woods. You kill the bear. "
                  "\nYou win :)")
        elif answer3 == "away":
            print("\nYou stumble away the best you can, but it's no match for the bear approaching rapidly."
                  " The bear catches up and you are terminated. \nYou lose :(")
        else:
            print("Not a valid option. You lose!")
            quit()
    elif answer2 == "rest":
        answer4 = input("\nYou fall asleep for hours only to wake up to a strange man watching you from behind a tree. "
                        "\nDo you approach the man or run away? Type 'approach' to approach or 'run' to run: ").lower()
        if answer4 == "approach":
            print("\nYou approached the man and he lures you to his cabin where you are never seen or heard from again."
                  "\nYou lose :(")
        elif answer4 == "run":
            print("\nYou run away as best as you can, and you come out on to road with a car approaching. "
                  "They stop and take you to safety. \nYou win :)")
        else:
            print("Not a valid option. You lose!")
            quit()
    else:
        print("Not a valid option. You lose!")
        quit()
elif answer1 == "right":
    answer5 = input("\nYou walk towards the light and see a castle as big as a mountain. "
                    "\nDo you knock on the door or do sneak around? Type 'knock' to knock around and 'sneak' to "
                    "sneak: ").lower()
    if answer5 == "knock":
        answer6 = input("\nYou knock on the door and woman who appears to be a witch opens the door. She invites you "
                        "in for dinner and shelter. \nDo you decline or accept? Type 'decline' to decline and 'accept' "
                        "to accept: ")
        if answer6 == "decline":
            print("\nYou decline the witches hospitality and she turns you into a potato for her soup for being rude. "
                  "\nYou lose :(")
        if answer6 == "accept":
            print("\nYou accept the witches hospitality and she gives you a warm meal and shelter until rescue comes"
                  " in the morning. \nYou win :)")
        else:
            print("Not a valid option. You lose!")
            quit()
    elif answer5 == "sneak":
        print("\nYou sneak around the castle only to fall into a river and drown. \nYou lose :(")
    else:
        print("Not a valid option. You lose!")
        quit()
else:
    print("Not a valid option. You lose!")
    quit()