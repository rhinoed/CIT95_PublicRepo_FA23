# Choose your path story
# For CIT 95 Giraffe Academy Assignment
# Inspired by Giraffe Academy "Madlibs" example
# by Mark Edmunds
# August 18, 2023.
import random

MAIN_STORY_STRINGS = [
    "Yor are standing at a crossroads. There is nothing behind you except the well worn path that led you here.\n"
    "In front of you the path continues,seemingly forever. But far in the distance you spot what looks like smoke.\n"
    "To your left there are some trees and through the trees you hear the sound of water.\n"
    "Looking to your right you see a path which leads to a well\n"
    "Out of your pocket you pull out a die. You have travel a long way and are weary. You decide to let chance decide "
    "your path\n"
    "You roll the die", "You reach the smoke and are horrified to see a small village in engulfed in flams\n"
                        "What do you run or help fight the fire\n",
    "You reach the water. Near the shore of river is a fishing pole and wood you could use for a fire\n"
    "There is also a boat. What do you do fish or take the boat \n",
    "You reach the well it is nealy empty except for one bucket full of water. As you are pull up the water a farmer "
    "approaches to get water for his horse\n"
    "What do you do take the water or give it to the farmer for his horse?:"]
PATH_STRINGS = ["The die shows 1 you go straight\n", "The die shows 2 you go left\n", "The die show 3 you go right\n"]
VILLAGE_OPTIONS = ["\nYou turn to run and are knocked to the ground and trampled to death by fleeing livestock\n",
                   "\nYou join the villagers in a fire line and save the village\n"]
RIVER_OPTIONS = ["\nYou catch loads of fish, and sleep by a warm fire\n",
                 "\nYou row the boat out to the middle of the river. It starts to leak and sinks and you drown\n"]
WELL_OPTIONS = [
    "\nYou take the water for yourself and as you are walking away the horse kicks you. You stumble and fall into the "
    "well. The farmer shout 'servers your right' and leaves you there\n",
    "\nYou share the water with the farmer and horse. the farmer is grateful and offers you a ride"]
CLOSING_STRINGS = ["\nAnd you live 'happy-ish' ever after", "\nTHE END"]

# main program sequence loops on 'y' from user
def main():
    ran_path = random.randint(0, 2)
    print(MAIN_STORY_STRINGS[0])
    print(PATH_STRINGS[ran_path])
    if ran_path == 0:
        your_path(ran_path)
    elif ran_path == 1:
        your_path(ran_path)
    else:
        your_path(ran_path)
    play_again = input("\nDo you want to play again? y/n: ")
    if play_again == "y" or play_again == "Y":
        main()
    else:
        print("Thanks for playing")

# pah chosen by ram_path in main
# the path determines the choices available to you
# // To Do: need to validate user input a 1 or 2 any number >2 will crash program
def your_path(path):
    if path == 0:
        print(MAIN_STORY_STRINGS[1])
        your_choice = int(input("\n Enter 1 to run or 2 help: "))
        print(VILLAGE_OPTIONS[your_choice - 1], CLOSING_STRINGS[0], CLOSING_STRINGS[1])
    elif path == 1:
        print(MAIN_STORY_STRINGS[2])
        your_choice = int(input("\n Enter 1 to fish or 2 to use boat: "))
        print(RIVER_OPTIONS[your_choice - 1], CLOSING_STRINGS[0], CLOSING_STRINGS[1])
    else:
        print(MAIN_STORY_STRINGS[3])
        your_choice = int(input("\n Enter 1 to take water or 2 share the water: "))
        print(WELL_OPTIONS[your_choice - 1], CLOSING_STRINGS[0], CLOSING_STRINGS[1])


main()
