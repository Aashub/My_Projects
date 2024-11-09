alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# to import logo from the art.py file
from  art import logo


print(logo)
# ceasar function to get input of text, the number of shift in letter and what do you want to do with text
# encode or decode
def caesar(plain_text, shift_amount, direction_txt):

  # check do you want to encode
  if direction_txt == "encode": 
    shifter = ""

    # loop through the text / then check the letter present in alphabet if present then go inside
    for index in plain_text:
      if index in alphabet:

        # store alphabet  index number in position and then by adding shift_amount with positon and store in 
        # shifter we get the result of encoding
        position = alphabet.index(index)
        shifter += alphabet[shift_amount + position]

      # if index is not present in alphabet then run this part where provided text store same to same without change
      else:
        shifter += index

    print(f"The encoded text is {shifter}")

  
  # similar process as we did in encoding
  elif direction_txt == "decode":
    unshifter = ""
    for jndex in plain_text:
      if jndex in alphabet:
        position = alphabet.index(jndex)
        unshifter += alphabet[position - shift_amount]

      else:
        unshifter += jndex
    print(f"The decoded text is {unshifter}")

should_continue = True

# create while loop to ask user do you want to continue coding or decoding of text
while should_continue == True:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  # to check the character shift if shift is greater then 26 then divide it by 26
  if shift > 26:
    sh = shift%26
    caesar(plain_text= text, shift_amount=sh, direction_txt= direction)
    print(sh)
  
  # else run normally
  elif shift < 26:
    sh = shift
    caesar(plain_text= text, shift_amount=sh, direction_txt= direction)

  # here we ask user to restart the the game or not
  restart = input("Do you want to restart the cipher text type 'yes' and 'no' \n").lower()
  if restart =="yes":
    should_continue

  elif restart == "no":
    should_continue = False
    print("Good Bye !")
  


