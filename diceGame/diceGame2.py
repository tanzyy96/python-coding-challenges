#bettingDiceGame
import random

rounds = 0
bank = 10.0
MAX = 3

def choosePlayer():
    player = input("User or Dealer wins?")
    while player!= "user" or "dealer":
        player = input("User or Dealer wins?")
    return player
        
    
def placeBet():
    bet = float(input("How much would you like to bet? The maximum bet is $3."))
    while bet >3:
        bet = float(input("How much would you like to bet? The maximum bet is $3."))
    return bet

def rollDice():
    user = random.randint(1,6)
    print("You rolled a", user ,"!")
    comp = random.randint(1,6)
    print("Dealer rolled a", comp , "!")
    if user > comp:
        print("You win!")
        return "user"
    elif comp> user:
        print("You lose!")
        return "dealer"
    else:
        print("It's a draw!")
        return "draw"

while True:
    choice = input("Would you like to roll the dice? Y/N") 
    if choice == 'Y':
        rounds+=1
        print("Round",rounds)
        myBet = placeBet()
        myPlayer = choosePlayer()
        if rollDice() == myPlayer():
            print("Nice bet! You win",myBet)
            bank+=myBet
        else:
            print("Try again next time...")
            bank-=myBet
        
    elif choice == 'N':
        print("Thanks for playing!")
        break
    else:
        print("Error. Please input 'Y' or 'N'.")

