print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")



 

level1 = input(
    "do you want to go through the bridge or go by different direction Y or N")

if (level1 == "Y"):

    level2 = input(
        "choose which root you want to go through by cave or hicking ")
    if (level2 == "cave"):

        level3 = input(
            "choose between three roots in the cave one two or three")
        if (level3 == "three"):
            print(
                "Congratulation you find the Captain Jack Sparrow lost treasures !"
            )

        elif (level3 == "two"):
            print(
                "game over you fall into the muddy area and did not find a way to out"
            )

        elif (level3 == "one"):
            print("game over you lost in the cave and did not find a way out")

    elif (level2 == "hicking"):
        print("game over land slide is happpened because of heavy rain ")

elif (level1 == "N"):
    print("game over you are captured by the pirates and they killed you")
