import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_images = [rock,paper,scissors]
user_choice =int(input("what do you user_choice? Type 0 for Rock, 1 for paper or 2 for scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("Invalid number, You lose!")
else:
    print(game_images[user_choice])

    computer = random.randint(0,2)
    print(f"computer chose")
    print(game_images[computer])


    if user_choice == computer:
        print("draw")
    elif user_choice == 0 and computer == 1:
        print("you lost")
    elif user_choice == 1 and computer == 0:
        print("you won")
    elif user_choice == 2 and computer == 0:
        print("you lost")
    elif user_choice == 0 and computer == 2:
        print("you won")
    elif user_choice == 1 and computer == 2:
        print("you lost")