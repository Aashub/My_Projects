from art import logo
from art import vs
from game_data import data
from replit import clear
import random


# get_data(data) function use data from the game_data file and assign it to below variable
def get_data(data):

  random_data = random.choice(data)
  name = random_data["name"]
  follower = random_data["follower_count"]
  description = random_data["description"]
  country = random_data["country"]

  return f"{name}, {description}, {country}", follower


# get_outPut() function assign its get_data() return value into  variables below, each time different
def get_output():
  input_data1, follower_data1 = get_data(data)
  input_data2, follower_data2 = get_data(data)

  return input_data1, input_data2, follower_data1, follower_data2


# here all return value is assign in this variables so get_winner can use them
input1, input2, foll1, foll2 = get_output()


# this function provide the winner
def get_winner(input1, input2, foll1, foll2, score):

  should_continue = True
  while should_continue == True:
    print(logo)
    print(f"Compare A: {input1}")

    print(vs)
    print(f"Against B: {input2}")

    check = input("Who has more Follower?, 'A' or 'B':").title()

    if foll1 > foll2 and check == "A":
      score += 1
      clear()
      print(f"You're Right!, Current Score:{score}")
      # here get_output() function calls and get new random data
      get_output()

    elif foll1 < foll2 and check == "B":
      score += 1
      clear()
      print(f"You're Right!, Current Score:{score}")
      get_output()

    elif foll1 > foll2 and check == "B":
      clear()
      print(logo)
      print(f"Sorry, That's Wrong. Final Score:{score}")
      should_continue = False

    elif foll1 < foll2 and check == "A":
      clear()
      print(logo)
      print(f"Sorry, That's Wrong. Final Score:{score}")
      should_continue = False

    elif foll1 == foll2:
      clear()
      print(
        f"Both Individual followers are same, Try Again. \nCurrent Score:{score} "
      )
      get_output()

    else:
      clear()
      print("Invalid Input, Try Again")
      print(f"Current Score:{score}")
      get_output()

    #the input and follower value are assignn here when get_output() function was called in if else statement.
    input1, input2, foll1, foll2 = get_output()


get_winner(input1, input2, foll1, foll2, score=0)
