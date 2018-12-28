import random

# enable loop
playAgain = True

while playAgain:
    ## 1.1 Create an array to store to store possible words ##
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

    # 1.2.2 Int: Number of guesses left

    # 1.2.3 List: Letters in answer

    # 1.2.4 String: Guessed letters --> we want to show which letters have already been guessed

    # 1.2.5 List: Stores state of hangman e.g. '__a__a_'

    keepGuessing = True
    while keepGuessing:
        print("\n//----------------------------------------------//")
        print("Hangman! I am thinking of a word:")
        # 1.2.6 print(''.join( <-- insert 1.2.5 here --> ))
        print("Number of guesses left:",count)
        print("You have guessed letters:",guessedLetters)
        print("Please select a letter between A-Z:")

        ## 1.3 Checking for Valid Guess ##
        while True:
            # 1.3.1 Input: guess in lower case
            # 1.3.2 Conditional: Check if entry is a (1)SINGLE, (2)ALPHABETICAL (use .alpha()) and has not been (3)GUESSED before

        print("checking...")
        ## 1.4 Check for Letters ##
        # 1.4.1 Conditional: If guess is not in original word, increment guess count

        # 1.4.2 Conditional: Else use loop to update state of hangman

        # 1.4.3 Print guessed Letters

        ## 1.5 Check if Game Finished ##
        # 1.5.1 Conditional: Check if guess count has finished

        # 1.5.2 Conditional: Check if entire word has been completed

    ## 1.6 Ask if User wants to Play Again ##
