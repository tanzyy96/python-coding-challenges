import random
from random_word import RandomWords

# enable loop
playAgain = True

while playAgain:
    ## 1.1 Create an array to store possible words ##
    words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                     "computer", "python", "program", "glasses", "sweatshirt",
                     "sweatpants", "mattress", "friends", "clocks", "biology",
                     "algebra", "suitcase", "knives", "ninjas", "shampoo"]

    print("Welcome to Hangman!")
    print("A word will be chosen at random.")
    print("Try to guess the word correctly letter by letter")
    print("before you run out of attempts. Good luck!")

    ## 1.2 Setting up Variables ##
    # 1.2.1 String: Pick a random answer
    chosenWord = random.choice(words)
    # 1.2.2 Int: Number of guesses left
    count = 8
    # 1.2.3 List: Letters in answer
    guessArray = list(chosenWord)
    # 1.2.4 String: Guessed letters --> we want to show which letters have already been guessed
    guessedLetters = ""
    # 1.2.5 List: Stores state of hangman e.g. '__a__a_'
    chosenWordArray =[]
    for letter in chosenWord:
        chosenWordArray.append("_")


    keepGuessing = True
    while keepGuessing:
        print("\n//----------------------------------------------//")
        print("Hangman! I am thinking of a word:")
        print(''.join(chosenWordArray)) # 1.2.6
        print("Number of guesses left:",count)
        print("You have guessed letters:",guessedLetters)
        print("Please select a letter between A-Z:")

        ## 1.3 Checking for Valid Guess ##
        while True:
            # 1.3.1 Input: guess in lower case
            guess = input().lower()
            # 1.3.2 Conditional: Check if entry is a (1)SINGLE, (2)ALPHABETICAL (use .alpha()) and has not been (3)GUESSED before
            if guess.isalpha() and len(guess) == 1: # check if single letter
                if guess not in guessedLetters: # check if new letter
                    print("Valid entry.\n")
                    break
                else:
                    print("You have already guessed that letter. Please try again.")
            else:
                print("Error. Please select a single letter between A-Z")

        ## 1.4 Check for Letters ##
        # 1.4.1 Conditional: If guess is not in original word, increment guess count
        if guess not in guessArray:
            print("No letter found!")
            count-=1
        # 1.4.2 Conditional: Else use loop to update state of hangman
        else:
            print("A letter was found!")
            for i in range(len(guessArray)):
                if chosenWordArray[i] == '_' and guessArray[i] == guess:
                    chosenWordArray[i] = guess
                print(chosenWordArray[i], end='')   # 1.4.3 Print guessed letters
        guessedLetters += guess + ' '
        print('\n')

        ## 1.5 Check if Game Finished ##
        # 1.5.1 Conditional: Check if guess count has finished
        if count == 0:
            print("You have ran out of guesses!")
            print("The word is", chosenWord)
            break
        # 1.5.2 Conditional: Check if entire word has been completed
        if chosenWordArray == guessArray:
            print('YOU GOT IT!!')
            break

    ## 1.6 Ask if User wants to Play Again ##
    choice = input("Would you like to play again? Y/N")
    if choice != 'Y' and choice != 'N':
        choice = input("Would you like to play again? Y/N")
    elif choice == 'N':
        playAgain = False
