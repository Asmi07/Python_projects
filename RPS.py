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

choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(choices[computer_choice])
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(choices[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(choices[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice == computer_choice:
        print("It's a draw!")

# choices = [rock,paper,scissors]
# player_choice = int(input("What do you want to choose? Enter 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

# computer_choice = random.randint(0,2)

# print(choices[player_choice])
# print(choices[computer_choice])

# outcome = ["It is a draw!", "You win!", "You lose!"]
# print(outcome[player_choice - computer_choice])




