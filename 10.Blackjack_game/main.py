
from art import logo
from replit import clear
import sys

import random


print(logo)

# this fucntion assign dealer and player their cards also let them assign one extra card to retrive
def get_deal():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  
  player_value = random.sample(cards, 2)
  player_value_incr = random.sample(cards,1)
  dealer_value = random.sample(cards, 2)
  dealer_value_incr = random.sample(cards, 1)
  Deal = {"key1" : player_value, "key2" : dealer_value}

  # returing the pl cards and dealer cards and also extra cards that can help later
  return Deal["key1"],Deal["key2"],player_value_incr,dealer_value_incr


START = input("Welcome to Blackjack game type start to start the Deal :").capitalize()

# assigning the get_deal value to all this parameter
player_value,dealer_value,player_hit_value,dealer_hit_value = get_deal()


# when user type start then it start the game
if START == "START":
  get_deal()

else:
  print("Invalid Input Provide necessay input to start Game.")


#  In this fucntion dealer, one value is hide by the dash so the player dont see it.
def get_dealer(dealer_value):

  for index, items in enumerate(dealer_value):
    if index == 0:
      index_value = dealer_value[index]
      dealer_value[index] = "_"
  
  return dealer_value,index_value

# here hide(dash) value and hidden value both assign to the given parameter
dealer_dash_value, original_value = get_dealer(dealer_value)

# in this fucntion the cards value are called every time this fucntion called.
def print_cards():
  print("the player cards are :")
  print(player_value)
  print("The dealer cards are :")
  print(dealer_dash_value)


should_continue_player = True

# run this while loop until its conditin dont turn into false
while should_continue_player == True:

  clear()
  print_cards()
  # ask user to decide what he wants to do.
  ask_player = input("decide what you want to choose to win game 'Hit' = increase_hand_value,'Stand' = keep_current_hand_value :").title()

  
  total_pl_value = 0
  # if player decide to hit then the new card is drawn from the deck(cards)
  if ask_player == "Hit":
    player_value.extend(player_hit_value)

    # calculate total player value 
    for index, score in enumerate(player_value):
      total_pl_value += player_value[index]
      
  
  # if player decide to stand then it stop taking new cards and calculate and total it
  elif ask_player == "Stand":
    print("not more cards")
    for index, score in enumerate(player_value):
      total_pl_value += player_value[index]
    should_continue_player = False   

  else:
    print("Invalid Input Provide right Input")


should_continue_dealer = True

total_dealer_value = 0
dealer_dash_value[0] = original_value

blackjack = "blackjack"

# run while loop until the condition turn inot false
while should_continue_dealer == True:
  
  # initial dealer value is added to check some starting condition to win for dealer and player
  for index, num in enumerate(dealer_dash_value):
    total_dealer_value += num
 
  if total_dealer_value == 21:
    print(print_cards())
    print(f"The Dealer Won with {blackjack}!")
    should_continue_dealer = False
   

  elif total_dealer_value <= 17 and total_dealer_value <= 21  :
    if total_pl_value < total_dealer_value:
      print(f"The Dealer Won with {total_dealer_value}")
      should_continue_dealer = False
   
    # here the dealer new card(value) is assigned it 
    dealer_dash_value.extend(dealer_hit_value)

    # now the total dealer points is assigned to zero so further winning condition can be checked.
    total_dealer_value = 0

    # sum total dealer points 
    for index, num in enumerate(dealer_dash_value):
      if total_dealer_value <= 21 :
        total_dealer_value += num
      should_continue_dealer = False

      
  elif total_dealer_value > 17:
    should_continue_dealer = False

# this function provide the winner that we required.
def get_winner(dealer_points = total_dealer_value, player_points = total_pl_value):
    clear()
    if dealer_points == player_points:
      print(print_cards())
      print("Both sides have equal points The Game is Tie !")

    elif total_pl_value == 21:
      print(print_cards())
      print(f"The Player Won with {blackjack}!")
  

    elif player_points > dealer_points and player_points > 21:
       print(print_cards())
       print("The Player is busted so the Dealer Win!")
        
    elif player_points > dealer_points and player_points < 21:
      print(print_cards())
      print(f"The Player won with {player_points} points !")
      
    elif dealer_points > player_points and  dealer_points < 21 :
      print(print_cards())
      print(f"The Dealer won with {dealer_points} points !")

    
    elif dealer_points == 21:
      print(print_cards())
      print("The Dealer Won by Blackjack")

    
    elif dealer_points > 21:
      print(print_cards())
      print("The Dealer is Busted so The Player Won !")
      

get_winner(dealer_points = total_dealer_value, player_points = total_pl_value)

  
  
    
  
  
  
  