import random

# Declare globals
final = []
points = 0
roundNum = 1

# Open the dictionary, read out the words, split into a list and close the file
f = open("dictionary.txt")
words = f.read().split("\n")
f.close()

# Select a random word from the list
word = random.choice(words)

# Generate underscores corresponding to length of selected word and set up points
for index, letter in enumerate(word):
    final.append("_")
    points += 1

# Print underscores and welcome message
print(" ".join(final), end="\n\n")
print("Welcome to hangman! The word you'll be guessing is " + str(len(word)) + " letters long, so you have " + str(points) + " points. Let's get started...\n")

while(points > 0):
    # Prompt for input until they enter letter(s)
    print("--- Round " + str(roundNum) + " ---")
    guessed = input("Enter a letter to guess, or guess the entire word: ").upper()
    while(not guessed.isalpha()):
        error = "didn't enter anything" if len(guessed) == 0 else "can only enter letters, no symbols or numbers"
        guessed = input("Error: You " + error + ". Please enter a valid letter or word to guess: ").upper()
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
                
        
        print("You have " + str(points) + " points left.\n")
        print(" ".join(final), end="\n\n")
    
    # Otherwise, if they entered the right word, they win, otherwise they lose.        
    else:
        if guessed == word:
            for i in range(len(final)):
                final[i] = word[i].upper()
            break
        else:
            points = 0
    roundNum += 1

# If they have points left, they win. Otherwise, they lose.
if points > 0 :
    print("Well done, you won with " + str(points) + " points to spare!")
else:
    print("Oh dear, you lost! The final word was \"" + word.lower() + "\". Better luck next time!")
