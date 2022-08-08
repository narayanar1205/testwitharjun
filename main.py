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

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.: \n "))
computerChoice = random.randint(0,2)

if userChoice >=3 or userChoice < 0:
  print("Invalid input made you loose")
else:  
  print("You choose")
  if userChoice==0:
    print(rock)
  elif userChoice==1:
    print(paper)
  else:
    print(scissors)
  
  print("Computer choose")
  if computerChoice==0:
    print(rock)
  elif computerChoice==1:
    print(paper)
  else:
    print(scissors)
  if userChoice==0 and computerChoice==2:
    print("You won")
  elif userChoice==1 and computerChoice==0:
    print("You won")
  elif userChoice==2 and computerChoice==1:
    print("You Won")
  elif userChoice==computerChoice:
    print("It's a draw")
  else:
    print("You lost")