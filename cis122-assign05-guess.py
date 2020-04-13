'''
Author: Derek Martin
Credit: CIS 122
Description: Create a simple guessing game that prompts the user for a word and for guesses
'''

# Initlialize variables
guessed_letters = ""
correct_guesses = ""
wrong_guesses = ""
num_guesses = 0
unique_letters = ""
finished = False

# Enter word
word = str(input("Enter a guess word (blank to quit): "))

# Number of letters in word
num_letters_in_word = len(word)

# Quits if blank word
if (num_letters_in_word != 0):

    # Determine unique letters in guess word
    for i in range(num_letters_in_word):
        if ((word[i] in word) and word[i] not in unique_letters):
            unique_letters += word[i]
            num_unique_letters = len(unique_letters)

    # Main while prompt loop
    while (not finished):
        
        # Enter letter guess, reprompt if multiple letter input
        letter_guess = str(input("Enter a guess letter (blank to quit): "))
        while (len(letter_guess) > 1):
            print("\t> Only enter a single letter")
            letter_guess = str(input("Enter letter: "))

        # Quit if blank letter
        if (len(letter_guess) != 0):
                    
            # Letter found ONCE and/or already guessed?
            if (letter_guess in guessed_letters):
                if (letter_guess in unique_letters):
                    print("\t>", letter_guess, "already guessed and found")
                else:
                    print("\t>", letter_guess, "already guessed and not found")    
            else:
                if (letter_guess in unique_letters):
                    print("\t>", letter_guess, "found")
                    correct_guesses += letter_guess
                else:
                    print("\t>", letter_guess, "not found")
                    wrong_guesses += letter_guess

            # Number of guesses
            num_guesses += 1

            # Vault of guessed letters
            if (letter_guess not in guessed_letters):
                guessed_letters += letter_guess
                        
            # Print guessed so far
            print("\t> Guesses so far:", guessed_letters)

            # Does guessed letters == unique letters
            for i in range(num_unique_letters):
                if (unique_letters[i] not in guessed_letters):
                    finished = False
                    break
                else:
                    finished = True
                    
        else:
            break

    # Final results
    if (finished):
        print("\t> All letters found")
        print()
        print("*** Results ***")
        print("Word:\t\t", word)
        print("Matched:\t", correct_guesses)
        print("Unmatched:\t", wrong_guesses)
        print("Guesses:\t", num_guesses)
