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

print("Welcome to Josh's Rock / Paper / Scissors PYTHON game.")

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if player >= 0 and player <= 2:
  if player == 0:
    player = rock
  elif player == 1:
    player = paper
  elif player == 2:
    player = scissors

  import random
  
  computer = random.randint(0, 2)
  if computer == 0:
    computer = rock
  elif computer == 1:
    computer = paper
  elif computer == 2:
    computer = scissors

  win = (player == rock and computer == scissors) or (player == paper and computer == rock) or (player == scissors and computer == paper)  

  print(player)
  print(f"Computer chose: {computer}")

  if win == True:
    print("You win!")
  elif player == computer:
    print("It's a draw")
  else:
    print("You lose")    
else:
  print("You typed an invalid number, you lose!")
  
