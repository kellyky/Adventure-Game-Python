import time
import random


villain = random.choice(["oceanographer", "inept but evil pirate", "tax "
                         "collecter", "car salesman", "baby shark"])

weapons = ["dagger"]

intro_narrative = ["You find yourself standing in an open field, filled with "
                   "grass and yellow wildflowers.", "Rumor has it that a " +
                   villain + " is somewhere around here, and has "
                   " been terrifying the nearby village.", "In front of you "
                   "is a house.", "In your hand you hold your trusty (but "
                   "ineffective) dagger."]

field_narrative = ["", "Enter 1 to knock on the door of the house.",
                   "Enter 2 to peer into the cave.", "What would you like "
                   "to do?"]

house_narrative = ["You approach the door of the house.", "You are about to "
                   "enter and out steps a " + villain + ".", "Eep! This is "
                   "the " + villain + "'s house!", "The " + villain + " "
                   "attacks you!"]

cave_narrative = ["You peer cautiously into the cave.", "It turns out to be "
                  "only a very small cave.", "Your eye catches a glint of "
                  "metal behind a rock.", "You have found the magical Sword "
                  "of Ogoroth!", "You discard your silly old dagger and take "
                  "the sword with you.", "You walk back out to the field."]

flees_narrative = ["You run back into the field.", "Luckily, you don't seem "
                   "to have been followed."]

defeat_narrative = ["You do your best...", "but your dagger is no match for "
                    "the " + villain + ".", "You have been defeated!"]

victory_narrative = ["As the " + villain + " moves to attack, you unsheath "
                     "your new sword.", "The Sword of Ogoroth shines brightly "
                     "in your hand as you brace yourself for the attack.",
                     "But the" + villain + " takes one look at your shiny new "
                     "toy and runs away!", "You have rid the town of the " +
                     villain + ". You are victoroius!"]


def print_pause(text):
    print(text)
    time.sleep(1)


def intro():
    for line in intro_narrative:
        print_pause(line)


def not_an_option():
    print_pause("That's not an option.")


def field():
    for line in field_narrative:
        print_pause(line,)
    decision = input("(Please enter 1 or 2.)\n")
    if '1' in decision:
        house()
    elif '2' in decision:
        cave()
    else:
        not_an_option()
        field()


def cave():
    if 'sword' in weapons:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now. You walk back out to the "
                    "field.")
    else:
        for line in cave_narrative:
            print_pause(line)
        weapons.append("sword")
    field()


def house():
    for line in house_narrative:
        print_pause(line)
    if 'sword' in weapons:
        decision = input("Would you like to (1) fight or (2) run away?\n")
        if decision == '1':
            victory()
        elif decision == '2':
            flees()
        else:
            not_an_option()
            house()
    else:
        print_pause("You feel a bit under-prepared for this, what with only "
                    "having a tiny dagger.")
        decision = input("Would you like to (1) fight or (2) run away")
        if decision == '1':
            defeat()
        elif decision == '2':
            flees()
        else:
            print("That's not an option.")


def fight_input():
    decision = input("Would you like to (1) fight or (2) run away?")


def flees():
    for line in flees_narrative:
        print_pause(line)
    field()


def victory():
    for line in victory_narrative:
        print_pause(line)
    weapons.remove('sword')
    play_again()


def defeat():
    for line in defeat_narrative:
        print_pause(line)
    play_again()


def play_again():
    answer = input("Would you like to play again? y/n \n")
    if 'y' in answer:
        print_pause("Excellent! Restarting the game...")
        play_game()
    elif 'n' in answer:
        print_pause("Thank you for playing! See you next time.")
    else:
        not_an_option()
        play_again()


def play_game():
    intro()
    field()


play_game()
