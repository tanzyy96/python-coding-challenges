#HANGMAN
import random

playAgain = True

#main loop
while playAgain:
    #array to store possible words
    words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                     "computer", "python", "program", "glasses", "sweatshirt",
                     "sweatpants", "mattress", "friends", "clocks", "biology",
                     "algebra", "suitcase", "knives", "ninjas", "shampoo"]

    print("Welcome to Hangman!")
    print("A word will be chosen at random.")
    print("Try to guess the word correctly letter by letter")
    print("before you run out of attempts. Good luck!")

    #Setting up Variables
    chosenWord = random.choice(words)   # String: correct answer
    count = 8                           # Int: number of guesses left
    guessArray = list(chosenWord)       # List: letters in answer
    guessedLetters = ""                 # String: guessed letters
    chosenWordArray =[]                 # List: stores state of hangman game e.g. '__a__'
    for letter in chosenWord:
        chosenWordArray.append("_")


    #input guess
    while True:
        print("\n//----------------------------------------------//")
        print("Hangman! I am thinking of a word:")
        print(''.join(chosenWordArray))
        print("Number of guesses left:",count)
        print("You have guessed letters:",guessedLetters)
        print("Please select a letter between A-Z:")

        while True: #ensure valid guess entry
            guess = input().lower() # lower case
            if guess.isalpha() and len(guess) == 1: # check if single letter
                if guess not in guessedLetters: # check if new letter
                    print("Valid entry.\n")
                    break
                else:
                    print("You have already guessed that letter. Please try again.")
            else:
                print("Error. Please select a single letter between A-Z")

        if guess not in guessArray:
            print("No letter found!")
            count-=1
        else:
            print("A letter was found!")
            for i in range(len(guessArray)):
                if chosenWordArray[i] == '_' and guessArray[i] == guess:
                    chosenWordArray[i] = guess
                print(chosenWordArray[i], end='')
        guessedLetters += guess + ' '
        print('\n')
        #end condition
        if count == 0:
            print("You have ran out of guesses!")
            print("The word is", chosenWord)
            break
        if chosenWordArray == guessArray:
            print('YOU GOT IT!!')
            break
    choice = input("Would you like to play again? Y/N")
    if choice != 'Y' and choice != 'N':
        choice = input("Would you like to play again? Y/N")
    elif choice == 'N':
        playAgain = False

        #check guess
        '''
        print("checking..")
        oldWordArray = chosenWordArray.copy()
        for i in range(len(guessArray)):
            if chosenWordArray[i] == '_' and guessArray[i] == guess:
                chosenWordArray[i] = guess
            print(chosenWordArray[i], end='')
        print('\n')
        if oldWordArray == chosenWordArray:
            print("No letter found!")
            count-=1
        else:
            print("A letter was found!")
        guessedLetters += guess + ' '
        '''
