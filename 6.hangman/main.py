

import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

print(logo)
end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.

lives = 6

#Testing code


#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"you already {guess} guessed this letter try different one ")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    if guess not in chosen_word:
        print(
            f"You guessed this {guess} letter and it was in chosen word, you loose life"
        )
        print(lives)
        lives = lives - 1
        if lives == 0:
            print(f"You Lose, the actual word is {chosen_word}")
            end_of_game = True

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

    for index in reversed(range(len(stages))):
        if index == lives:
            print(stages[index])
