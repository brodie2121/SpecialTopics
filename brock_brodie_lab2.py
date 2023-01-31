import random

def display_title():
    print("Rolling the Dice")

def roll():
    return random.randint(1, 6)

def roll_dice():
    dice1 = roll()
    dice2 = roll()
    total = dice1 + dice2
    print("You rolled a {} and a {}, for a total of {}".format(dice1, dice2, total))
    if dice1 == dice2:
        if dice1 == 1:
            print("Snake eyes!")
        elif dice1 == 2:
            print("Ballerina!")
        elif dice1 == 4:
            print("Square pair!")
        elif dice1 == 6:
            print("Boxcars!")

def main():
    display_title()
    roll_again = 'y'
    while roll_again.lower() == 'y':
        roll_dice()
        roll_again = input("Roll the dice again? (y/n)")

if __name__ == '__main__':
    main()
