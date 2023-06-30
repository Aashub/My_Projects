from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

print("Welcome th the Secret Biding program")


# to store the name and amount element 
list_name = []
list_amount = []


# function to get the bider name and biding amount
def secret_biding(bider_name,biding_amount):

  
  list_amount.append(biding_amount)
  list_name.append(bider_name)

  # here the dictionary store the list element in it
  registration = {"Names": [list_name], "Amount": [list_amount]}

  result_amount = max(list_amount)

  # here the result amount index is stored in index finder so we can use it to find highest bider name
  index_finder = list_amount.index(result_amount)

  result_name = list_name[index_finder]

  return result_name,result_amount


biding = True


# while loop runs until the biding statement is not getted false
while biding is True:

    
    name = input("What is your name? : ").title()
    bid = int(input("What's your bid? : $"))
    other_bider = input(
        "Are there any other bidders ? Type 'Yes' or 'No'.").title()

    # storing the return value of secret_biding function
    name,amount = secret_biding(bider_name=name,
                      biding_amount=bid)


    
    if other_bider == "Yes":
        clear()
        secret_biding(bider_name=name,
                      biding_amount=bid
                      )
        
    elif other_bider == "No":
        clear()
        secret_biding(bider_name=name,
                      biding_amount=bid
                      )


        name,amount = secret_biding(bider_name=name,
                      biding_amount=bid
                      )
        print(f"The Winner is {name} with a bid of ${amount}.")
      

        biding = False

    else:
        clear()
        print("Invalid Input try Again !")
        
