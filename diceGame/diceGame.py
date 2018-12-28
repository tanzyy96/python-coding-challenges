#diceGame
import random

#1: computer rolls dice
#2: "Would you like to roll the dice? Y/N" -user input-
#3: Dice is rolled.
#   What happens when computer wins?
#   What happens when user wins?
#   Any other possible scenarios?

while True:
    choice = input("Would you like to roll the dice? Y/N") 
    if choice == 'Y':
        user = random.randint(1,6)
        print("You rolled a", user ,"!")
        comp = random.randint(1,6)
        print("Dealer rolled a", comp , "!")
        if user > comp:
            print("You win!")
        elif comp> user:
            print("You lose!")
        else:
            print("It's a draw!")
    elif choice == 'N':
        print("Thanks for playing!")
        break
    else:
        print("Error. Please input 'Y' or 'N'.")
