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

import random

choice = int(input("Time for some fun!\nLet's play a game of Rock, Paper, Scissors.\n\nAre you ready?\nType 0 for rock, 1 for paper or 2 for scissors: "))

if choice != 0 or choice !=1 or choice !=2:
  print("Invalid entry, you LOSE!")

else:
 options = [rock, paper, scissors]

 player_choice = options[choice]
 print(player_choice)

 print("\nComputer chose:")
 i = random.randint(0, 2)
 computer_choice = options[i]
 print(computer_choice)

 if choice == 0 and i == 0:
  print("It's a draw")
 elif choice == 0 and i == 1:
  print("You lose")
 elif choice == 0 and i == 2:
  print("You win")
 elif choice ==1 and i == 1:
  print("It's a draw")
 elif choice ==1 and i == 0:
  print("You win")
 elif choice ==1 and i == 2:
  print("You lose")
 elif choice ==2 and i == 2:
  print("It's a draw")
 elif choice ==2 and i == 1:
  print("You win")
 elif choice ==2 and i == 0:
  print("You lose")




