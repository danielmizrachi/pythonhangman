"""

*** Python Hangman ***

* Author: Daniel Mizrachi
* Date Written: 2016-06-29
* Purpose: A basic text based hangman game written in Python
* Platform Compatibility: All machines capable of running any version of Python 3
* Updated and pushed to Git: 2016-06-30

"""

import random
import rawinput

# Define functions
def getContentsAsList(filename, delimiter):
    # Open a file, read it and split it into a list using the specified delimiter, then return this list
    f = open(filename)
    fileList = f.read().split(delimiter)
    f.close()
    return fileList
def printList(lst, delimiter=" ", end="\n"):
    if type(lst) == list and type(delimiter) == str:
        # Join the list into a string using the specified delimiter and print the result
        print(delimiter.join(lst), end=end)
    else:
        raise SyntaxError("printList requires a list and string object.")

# Declare globals
final = []
points = roundNum = 0

# Prompt them to choose whether to play the game or view the help until they enter a valid command
cmd = input("Welcome. Would you like to:\n1) Play the game\n2) View the help\n3) View the manual\nSelect an option by entering its number: ")
while cmd != "1" and cmd != "2" and cmd != "3":
    cmd = input("Error: You didn't enter a valid option number. Would you like to:\n1) Play the game\n2) View the help")

if cmd == "1":
    print("\n--- NEW GAME ---\n")
    
    # Open the dictionary, read out the words, split into a list and close the file
    words = getContentsAsList("dictionary.txt", "\n")

    # Select a random word from the list
    word = random.choice(words)

    # Generate underscores corresponding to length of selected word and set up points
    for index, letter in enumerate(word):
        final.append("_")
        points += 1

    # Print underscores and welcome message
    printList(final, end="\n\n")
    print("Welcome to hangman! The word you'll be guessing is " + str(len(word)) + " letters long, so you have " + str(points) + " points. Let's get started...\n")

    while(points > 0):
        roundNum += 1
        
        # Prompt for input until they enter letter(s)
        print("--- Round " + str(roundNum) + " ---")
        guessed = rawinput.word("Enter a letter to guess, or guess the entire word: ", "Please enter a valid letter or word to guess: ")
        print("")

        # If they enter a single, correct letter, add it to the final string.
        if len(guessed) == 1:
            correct = False
            
            # For each letter in the word, if this letter is what they guessed, then set the corresponding underscore in the final word to that letter.
            for index, letter in enumerate(word):
                if letter == guessed:
                    final[index] = letter
                    correct = True
            
            # Tell them whether the round was successful or not, deduct a point if not
            if(correct):
                print("Correct! ", end="")
                if "".join(final) == word:
                    break
            else:
                points -= 1
                if points == 0:
                    break
                else:
                    print("Incorrect! ", end="")

            # Tell them how many points they have left and display their progress
            print("You have " + str(points) + " points left.\n")
            printList(final, end="\n\n")
        
        # Otherwise, if they entered the right word, they win, otherwise they lose.        
        else:
            if guessed == word:
                for i in range(len(final)):
                    final[i] = word[i].upper()
            else:
                points = 0
            break

    print("--- *** ---\n")
    # If they have points left, they win. Otherwise, they lose.
    if points > 0:
        print("Well done, you won in " + str(roundNum) + " rounds, with " + str(points) + " out of " + str(len(word)) + " points to spare!\n")
        printList(final)
    else:
        print("Oh dear, you lost! The final word was \"" + word.lower() + "\". Better luck next time!")

    print("\n--- GAME OVER ---\n")

elif cmd == "2":
    # Print the contents of the help file
    helpFile = open("help.txt")
    print("\n" + helpFile.read())
    helpFile.close()

else:
    # Print the contents of the manual file
    manual = open("manual.txt")
    print("\n" + manual.read())
    manual.close()
