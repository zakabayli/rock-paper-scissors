import random
import sys
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

game_images = [rock, paper, scissors]
# player chooses it's decision
user_choice = int(input("Please choose: 0 for Rock, 1 for Paper or 2 Scissors \n"))
if user_choice <= 2 and user_choice >= 0:
    print(f"you chose: {game_images[user_choice]}")

elif user_choice > 2 or user_choice <0:
    print("Invalid choice")
    sys.exit()

# computer randomly chooses it's decision
computer_choice = random.randint(0, 2)
print(f"Computer chose {game_images[computer_choice]}")

if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif computer_choice == 2 and user_choice == 0:
    print("You win!")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice < computer_choice:
    print("You lose!")


