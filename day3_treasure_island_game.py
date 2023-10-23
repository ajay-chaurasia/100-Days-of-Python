# Control flow in Python with if-else
# if condition:
#     do this
# else:
#     do this

# Nested if-else
# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

# if / elif / else
# if condition1:
#     do this
# elif condition2:
#     do this
# else:
#     do this

# AND | OR | NOT
# if condition1 and condition2 and condition3
# if condition1 or condition2
# if not condition1

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

life = 3
message = "lives"
while life > 0:
    if life == 1:
        message = "life"
    print(f"\n\n\n\nYou have {life} {message} left!")
    if not input("\nYou're at a cross road. Where do you want to go?\nType \"left\" or \"right\" ").lower() == "left":
        print("You fall into a hole. Game Over!")
        life -= 1
    elif not input("\nYou have arrived at a lake.\nThere is an island in the middle of the lake.\nDo you want to \"wait\" for a boat or \"swim\" to the island? ").lower() == "wait":
        print("You are attacked by Crocodiles. Game Over!")
        life -= 1
    else:
        choice = input("\nOn the island you see three doors - \"Red\", \"Yellow\" and \"Blue\".\nWhich door do you open? ").lower()
        if choice == "blue":
            print("\n\nCongratulations!\nYou found the hidden treasure of King Tottem!")
            break
        elif choice == "red":
            print("You have opened the room of fire!\nGAME OVER!")
            life -= 1
        elif choice == "yellow":
            print("You have opened the room full of beasts!\nGAME OVER!")
            life -= 1
        else:
            print("This isn't a door!\nGAME OVER!")
            life -= 1

print("\nThank you for playing!")
    
