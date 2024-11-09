#Number Guessing Game Objectives:

from art import logo
import random
from replit import clear


Number = random.randint(1, 100)
chances = [11, 6]


# definning fucntion to start the game
def start_game(Number):
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")

    # definning function to restart the game
    def Restart():
        restart = input(
            "Do you want to play another game! type 'y' or 'n'").title()

        # if restart = y then it clear screen and call start_game(Number) function to restart game
        if restart == "Y":
            clear()
            print("\n")
            start_game(Number)

        # print game over after if restart = n
        elif restart == "N":
            clear()
            print("\nGame Over!")

    # definning the get winner fucntion which can provide the winner 
    def get_winner(left_chances, answer):

        should_continue = True
        while should_continue == True:
          
            # substract chances so if game is over then provide the output
            left_chances = left_chances - 1
            if left_chances == 0:
                print("Game Over, you lost all chances to guess the anwser.")
                Restart()
                should_continue = False

            # if left chances are greater than zero runs until it became zero and than stop
            elif left_chances > 0:
                print(f"You have {left_chances} left to guess a number. ")
                guess = int(input("Make a guess:"))

                if guess > answer:
                    print("Too High, Try Again.")

                elif guess < answer:
                    print("Too Low, Try Again.")
      
                elif guess == answer:
                    print(f"You got it, the actual answer is {Number}")
                    Restart()
                    should_continue = False

    # here user decide difficulty of the game
    decide_difficulty = input(
        "Choose a difficulty type 'easy' or 'hard':").title()

    if decide_difficulty == "Easy":
        get_winner(left_chances=chances[0], answer=Number)

    elif decide_difficulty == "Hard":
        get_winner(left_chances=chances[1], answer=Number)

    else:
        clear()
        print(logo)
        print("Invalid Input, Try Again!")
        start_game(Number)

# calling the function and starting the game
start_game(Number)
