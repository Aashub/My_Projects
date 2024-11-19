import art
import random
from game_data import  data

Compare_A = []
Compare_B = []

def play_higher_lower():
    """this function starts the higher lower game for the first time"""
    score = 0
    iterate_for_compare_list= 0

    def data_for_comparison(score, iterate_for_comp_list):
        """this function provide data for comparison so we can check who has more followers in return value"""

        print(art.logo)
        if score >= 1:

            print(f"You're right!, Current score: {score}")

        # here when every time loops run it prints the value of imported game data file and///

        # append the value of follower in new list compare_A and compare_B and///

        # iterate_for_comp_list is used to updated new follower value in list so later it being compared to///
        # check who has more follower
        for to_compare in range(0,2):

            if to_compare == 0:
                random_data = random.choice(data)

                print(f"Compare A: {random_data["name"]}, {random_data["description"]}, {random_data["country"]}")
                Compare_A.append(random_data["follower_count"])
                follower_valueOF_a = Compare_A[iterate_for_comp_list]

            elif to_compare == 1:
                random_data = random.choice(data)

                print(art.vs)
                print(f"Compare B: {random_data["name"]}, {random_data["description"]}, {random_data["country"]}")
                Compare_B.append(random_data["follower_count"])
                follower_valueOF_b = Compare_B[iterate_for_comp_list]

        return follower_valueOF_a, follower_valueOF_b

    def restart_game():
        """this function restart or stop the game as per user input!"""
        should_continue_for_restart = True

        while should_continue_for_restart:
            restart = input("Do you want to Play Higher Lower game Again Type\n'y' for Yes and 'N' for No : ").lower()

            if restart == "y":
                print("\n" * 20)
                play_higher_lower()

            elif restart == "n":
                print("Thanks for playing this game, Have a Nice Day!")
                exit()

            else:
                print("Invalid Input!, Please try again!")

    A, B = data_for_comparison(score, iterate_for_compare_list)

    should_continue = True

    # here loop will run until user don't guess any wrong value.
    while should_continue:

        comparison = input("who has more followers? Type 'A' or 'B': ").lower()

        if comparison == "a":

            if A > B:
                score += 1
                iterate_for_compare_list += 1
                print("\n" * 20)
                A, B = data_for_comparison(score,iterate_for_compare_list)

            elif A < B:
                print("\n" * 20)
                print(art.logo)
                print(f"Sorry, that's wrong. Final score: {score}")
                restart_game()

        elif comparison == "b":

            if A < B:
                score += 1
                iterate_for_compare_list += 1
                print("\n" * 20)
                A, B  = data_for_comparison(score, iterate_for_compare_list)

            elif A > B:
                print("\n" * 20)
                print(art.logo)
                print(f"Sorry, that's wrong. Final score: {score}")
                restart_game()

            elif A == B:
                iterate_for_compare_list += 1
                print("\n" * 20)
                A, B = data_for_comparison(score, iterate_for_compare_list)

        else:
            print("Invalid Input, Please provide correct Input!\n")

play_higher_lower()




#_______________________________________________old higher or lower game code created previously___________________________________________





# from art import logo
# from art import vs
# from game_data import data
# from replit import clear
# import random


# # get_data(data) function use data from the game_data file and assign it to below variable
# def get_data(data):

#   random_data = random.choice(data)
#   name = random_data["name"]
#   follower = random_data["follower_count"]
#   description = random_data["description"]
#   country = random_data["country"]

#   return f"{name}, {description}, {country}", follower


# # get_outPut() function assign its get_data() return value into  variables below, each time different
# def get_output():
#   input_data1, follower_data1 = get_data(data)
#   input_data2, follower_data2 = get_data(data)

#   return input_data1, input_data2, follower_data1, follower_data2


# # here all return value is assign in this variables so get_winner can use them
# input1, input2, foll1, foll2 = get_output()


# # this function provide the winner
# def get_winner(input1, input2, foll1, foll2, score):

#   should_continue = True
#   while should_continue == True:
#     print(logo)
#     print(f"Compare A: {input1}")

#     print(vs)
#     print(f"Against B: {input2}")

#     check = input("Who has more Follower?, 'A' or 'B':").title()

#     if foll1 > foll2 and check == "A":
#       score += 1
#       clear()
#       print(f"You're Right!, Current Score:{score}")
#       # here get_output() function calls and get new random data
#       get_output()

#     elif foll1 < foll2 and check == "B":
#       score += 1
#       clear()
#       print(f"You're Right!, Current Score:{score}")
#       get_output()

#     elif foll1 > foll2 and check == "B":
#       clear()
#       print(logo)
#       print(f"Sorry, That's Wrong. Final Score:{score}")
#       should_continue = False

#     elif foll1 < foll2 and check == "A":
#       clear()
#       print(logo)
#       print(f"Sorry, That's Wrong. Final Score:{score}")
#       should_continue = False

#     elif foll1 == foll2:
#       clear()
#       print(
#         f"Both Individual followers are same, Try Again. \nCurrent Score:{score} "
#       )
#       get_output()

#     else:
#       clear()
#       print("Invalid Input, Try Again")
#       print(f"Current Score:{score}")
#       get_output()

#     #the input and follower value are assignn here when get_output() function was called in if else statement.
#     input1, input2, foll1, foll2 = get_output()


# get_winner(input1, input2, foll1, foll2, score=0)
