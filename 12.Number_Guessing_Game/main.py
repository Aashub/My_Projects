import art
import random

def play_Number_guessing_game():

    """this functions basically start this game every time this function is being called."""
    level_of_difficulty = {"easy": 10, "moderate": 7, "hard": 5}

    def restarting_Number_Guessing_Game():
        """this function restart the number guessing game once again"""

        should_continue = True
        while should_continue:
            restart_game = input("Do you want to play this game again?\ntype 'y' for Yes and 'n' for No ").lower()

            if restart_game == 'y':
                print("\n" * 20)
                play_Number_guessing_game()

            elif restart_game == 'n':
                print("Thank you for playing this game")
                exit()

            else:
                print("Incorrect Input, Please provide correct input!")

    def find_the_answer(left_attempt, correct_answer):
        """this function find out the correct guess"""

        print(f"You have {left_attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == correct_answer:
            print(f"You got it! The answer was {correct_answer}\n")
            restarting_Number_Guessing_Game()

        elif guess > correct_answer:
            print("Too High.")

        elif guess < correct_answer:
            print("Too Low.")

        else:
            print("Incorrect Input, Please provide correct input!")

    def choose_difficulty():
        """this function helps us to decide the difficulty level in which we want to play the game"""
        difficulty_level = input("Choose a difficulty. Type 'easy', 'moderate' or 'hard': ").lower()

        return  difficulty_level

    print(art.logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    correct_ans = random.randint(1, 100)
    print(f"Pssst, the correct answer is {correct_ans}")

    difficulty = choose_difficulty()

    # while loop runs until certain condition didn't became false
    should_continue = True
    while should_continue:

    # as per the difficulty level decided by the player find_the_answer functions call and every time a wrong guess is
    # is guessed then 1 attempt get subtracted if level_of_difficulty[_] became zero then player looses a game
        if difficulty == "easy":

            find_the_answer(left_attempt = level_of_difficulty["easy"], correct_answer = correct_ans)
            level_of_difficulty["easy"] -= 1


            if level_of_difficulty["easy"] == 0:
                print("You've run out of guesses, you lose.\n")
                restarting_Number_Guessing_Game()
            print("Guess again")

        elif difficulty == "moderate":

            find_the_answer(left_attempt = level_of_difficulty["moderate"],correct_answer =  correct_ans)
            level_of_difficulty["moderate"] -= 1

            if level_of_difficulty["moderate"] == 0:
                print("You've run out of guesses, you lose.\n")
                restarting_Number_Guessing_Game()
            print("Guess again")

        elif difficulty == "hard":

            find_the_answer(left_attempt = level_of_difficulty["hard"],correct_answer =  correct_ans)
            level_of_difficulty["hard"] -= 1

            if level_of_difficulty["hard"] == 0:
                print("You've run out of guesses, you lose.\n")
                restarting_Number_Guessing_Game()
            print("Guess again")

        else:
            print("Incorrect Input, Please provide correct Input!")
            difficulty = choose_difficulty()


play_Number_guessing_game()



#_______________________________________________old_number_guessing_code_created_previously___________________________________________

# #Number Guessing Game Objectives:

# from art import logo
# import random
# from replit import clear


# Number = random.randint(1, 100)
# chances = [11, 6]


# # definning fucntion to start the game
# def start_game(Number):
#     print(logo)
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 to 100.")

#     # definning function to restart the game
#     def Restart():
#         restart = input(
#             "Do you want to play another game! type 'y' or 'n'").title()

#         # if restart = y then it clear screen and call start_game(Number) function to restart game
#         if restart == "Y":
#             clear()
#             print("\n")
#             start_game(Number)

#         # print game over after if restart = n
#         elif restart == "N":
#             clear()
#             print("\nGame Over!")

#     # definning the get winner fucntion which can provide the winner 
#     def get_winner(left_chances, answer):

#         should_continue = True
#         while should_continue == True:
          
#             # substract chances so if game is over then provide the output
#             left_chances = left_chances - 1
#             if left_chances == 0:
#                 print("Game Over, you lost all chances to guess the anwser.")
#                 Restart()
#                 should_continue = False

#             # if left chances are greater than zero runs until it became zero and than stop
#             elif left_chances > 0:
#                 print(f"You have {left_chances} left to guess a number. ")
#                 guess = int(input("Make a guess:"))

#                 if guess > answer:
#                     print("Too High, Try Again.")

#                 elif guess < answer:
#                     print("Too Low, Try Again.")
      
#                 elif guess == answer:
#                     print(f"You got it, the actual answer is {Number}")
#                     Restart()
#                     should_continue = False

#     # here user decide difficulty of the game
#     decide_difficulty = input(
#         "Choose a difficulty type 'easy' or 'hard':").title()

#     if decide_difficulty == "Easy":
#         get_winner(left_chances=chances[0], answer=Number)

#     elif decide_difficulty == "Hard":
#         get_winner(left_chances=chances[1], answer=Number)

#     else:
#         clear()
#         print(logo)
#         print("Invalid Input, Try Again!")
#         start_game(Number)

# # calling the function and starting the game
# start_game(Number)
