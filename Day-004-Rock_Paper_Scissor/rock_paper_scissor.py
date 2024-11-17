roc = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

pap = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

sci = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
import os

moves = [roc, pap, sci]

userinput = int(input("provide user input in form of rock(0), paper(1), scissors(2)\n"))

computerinput = random.randint(0,2)

rock = 0
paper = 1
scissors = 2

if(userinput == rock or userinput == paper or userinput == scissors):
    if(userinput ==  computerinput):
        print(f"{moves[userinput]}\n YOU \n{moves[computerinput]}\n COMPUTER\n\n")
        print("The match is Draw!")
        
    elif(userinput == rock and computerinput == paper):    
        print(f"{moves[userinput]}\n YOU \n{moves[computerinput]}\n COMPUTER\n\n")
        print("You Lost!")

    elif(userinput == rock and computerinput == scissors):        
        print(f"{moves[userinput]}\n YOU \n{moves[computerinput]}\n COMPUTER\n\n")
        print("You Won!")

    elif(userinput == paper and computerinput == rock):    
        print(f"{moves[userinput]}\n YOU \n{moves[computerinput]}\n COMPUTER\n\n")
        print("You Won!")

    elif(userinput == paper and computerinput == scissors):        
        print(f"{moves[userinput]}\n YOU \n{moves[computerinput]}\n COMPUTER\n\n")
        print("You Lost!")
        
    elif(userinput == scissors and computerinput == rock):    
        print(f"{moves[userinput]}\n YOU \n{moves[computerinput]}\n COMPUTER\n\n")
        print("You Lost!")

    elif(userinput == scissors and computerinput == paper):        
        print(f"{moves[userinput]}\n YOU \n{moves[computerinput]}\n COMPUTER\n\n")
        print("You Won!")

elif(userinput > 2):  
    print("invalid input provide a right input")    
