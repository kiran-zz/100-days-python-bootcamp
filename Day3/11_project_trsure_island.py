print("Wecome to Treasure Island.")
print("Your mission is to find the tresure.")

choice1 = input('You\'re at a cross road. where do you want to go? Type "left" or "right".\n').lower()
if choice1 == "left":
    choice2 = input('you\'ve come to lake. There is an island in the middle of the lake. type "wait" to wait for boat. Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("red, yellow or blue \n").lower()
        if choice3 == "red":
            print("it's a room full of fire.game over")
        elif choice3 == "yellow":
                print("you won the tresure!.you win!")
        elif choice3 == "blue":
                print("you entered a room beast.Game over")
        else:
             print("door doesn't exist.game over")
    else:
         print("you attacked by trout. Game over")
else:
    print("you fell into a hole.Game over")




