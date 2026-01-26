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

images = [rock, paper, scissors]

# take user choice from the user
user_choice = int(input(
    "Please Enter your choice:\n"
    "Type 0 for Rock\n"
    "Type 1 for Paper\n"
    "Type 2 for Scissors\n> "
))

if (user_choice >= 3 or user_choice < 0):
    print("Please Enter a valid Choice!")
else:
    system_choice = random.randint(0, 2)

    print("\nYou Choose ->")
    print(images[user_choice])

    print("System Choose ->")
    print(images[system_choice])

    # write game logic here
    if (user_choice == system_choice):
        print("It's a draw!")
    elif (system_choice == 0 and user_choice == 2):
        print("You loose!")
    elif (system_choice == 2 and user_choice == 0):
        print("You won!")
    elif (system_choice > user_choice):
        print("You loose!")
    elif (user_choice > system_choice):
        print("You won!")
