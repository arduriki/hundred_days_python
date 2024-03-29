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

# Write your code below this line 👇

rock_paper_scissors = [rock, paper, scissors]

player_choose = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choose >= 0 and player_choose <= 2:
    player_move = rock_paper_scissors[player_choose]
else:
    print("Please, enter a correct number.")
    sys.exit()

cpu_choose = random.randint(0, 2)
cpu_move = rock_paper_scissors[cpu_choose]

if player_move == rock and cpu_move == scissors or player_move == paper and cpu_move == rock or player_move == scissors and cpu_move == paper:
    print("Player chooses:")
    print(player_move)
    print("CPU chooses:")
    print(cpu_move)
    print("Player wins!")
elif cpu_move == rock and player_move == scissors or cpu_move == paper and player_move == rock or cpu_move == scissors and player_move == paper:
    print("Player chooses:")
    print(player_move)
    print("CPU chooses:")
    print(cpu_move)
    print("CPU wins!")
else:
    print("Player chooses:")
    print(player_move)
    print("CPU chooses:")
    print(cpu_move)
    print("Tie game!")

"""------------
OTHER SOLUTION
------------"""

game_images = [rock, paper, scissors]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw")
