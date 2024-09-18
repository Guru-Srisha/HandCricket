import random

print("\n")
print("----------------------")
print("     Hand Cricket     ")
print("----------------------")
print("\n")
print("Rules:")
print("1. First, choose HEAD or TAIL during toss. If you win the toss, you will be given a chance to choose to BAT or BOWL first")
print("2. During your BATTING, you can input between 0 to 6. Your score goes on adding up. If your input and the computer's input is same, you will be bowled.")
print("3. During your BOWLING, you can input between 0 to 6 and the computer's score goes on adding up. If your input and the computer's input is same, the computer will be bowled")
print("4. Whoever has the highest score at the end wins!")
print("Good Luck :p")
print("\n")

print("How many overs you want to play?")
print("Enter a number:")
while True:
  try:
    overs = int(input())
    break
  except ValueError:
    print("Invalid input. Enter a number:")
print("\n")

print("Time to toss!")
print("1. HEAD")
print("2. TAIL")
print("Enter 1 or 2:")
while True:
  try:
    playerCall=int(input())
    if 1 <= playerCall <= 2:
      break
    else:
      print("Invalid input. Enter 1 or 2:")
  except ValueError:
    print("Invalid input. Enter 1 or 2:")
actualToss=random.randrange(1,3,1)  # (inclusive left range,exclusive right range,step)
print("\n")

if playerCall==actualToss:
  print("You won the toss!")
  print("Choose to BAT or BOWL")
  print("1. BAT")
  print("2. BOWL")
  print("Enter 1 or 2:")
  while True:
    try:
      bob=int(input())
      if 1 <= bob <= 2:
        break
      else:
        print("Invalid input. Enter 1 or 2:")
    except ValueError:
      print("Invalid input. Enter 1 or 2:")
  if bob==1:
    print("You choose to BAT and computer has to BOWL")
  else:
    print("You choose to BOWL and computer has to BAT")
else:
  print("You lost the toss ;-;")
  bob=random.randrange(1,3,1)
  if bob==2:
    print("Computer chooses to BAT and you have to BOWL")
  else:
    print("Computer chooses to BOWL and you have to BAT")
print("\n")

playerScore=0
computerScore=0
# First innings
if bob==1:
  # Player BATTING
  print("Your BATTING begins!")
  over=0
  ball=1
  while over<overs:
    print("\n")
    print(f"Ball {over}.{ball}:")
    print("Enter a number between 0 to 6:")
    while True:
      try:
        playerInput = int(input())
        if 0 <= playerInput <= 6:
          break
        else:
          print("Invalid input. Enter a number between 0 to 6:")
      except ValueError:
        print("Invalid input. Enter a number between 0 to 6:")
    computerInput=random.randrange(0,7,1)
    print(f"Your input: {playerInput}")
    print(f"Computer input: {computerInput}")
    if playerInput==computerInput:
      print("\n")
      print("You got bowled :(")
      print(f"Your score: {playerScore}")
      print(f"Computer needs to score {playerScore+1} to win")
      break
    else:
      playerScore=playerScore+playerInput
      print(f"Your score: {playerScore}")
    ball=ball+1
    if ball==7:
      print(f"Over {over+1} completed.")
      ball=0
      over=over+1

else:
  # Player BOWLING
  print("\n")
  print("Your BOWLING begins!")
  over=0
  ball=1
  while over<overs:
    print("\n")
    print(f"Ball {over}.{ball}:")
    print("Enter a number between 0 to 6:")
    while True:
      try:
        playerInput = int(input())
        if 0 <= playerInput <= 6:
          break
        else:
          print("Invalid input. Enter a number between 0 to 6:")
      except ValueError:
        print("Invalid input. Enter a number between 0 to 6:")
    computerInput=random.randrange(0,7,1)
    print(f"Your input: {playerInput}")
    print(f"Computer input: {computerInput}")
    if playerInput==computerInput:
      print("\n")
      print("You bowled computer!")
      print(f"Computer score: {computerScore}")
      print("\n")
      print(f"You need to score {computerScore+1} to win")
      break
    else:
      computerScore=computerScore+computerInput
      print(f"Computer score: {computerScore}")
    ball=ball+1
    if ball==7:
      print(f"Over {over+1} completed.")
      ball=0
      over=over+1
  if over+ball > overs:
    print("\n")
    print(f"You need to score {computerScore + 1} to win")
  print("End of innings")

# Second innings
if bob==1:
  # Player BOWLING
  print("\n")
  print("Your BOWLING begins!")
  over=0
  ball=1
  while over<overs:
    print("\n")
    print(f"Ball {over}.{ball}:")
    print("Enter a number between 0 to 6:")
    while True:
      try:
        playerInput = int(input())
        if 0 <= playerInput <= 6:
          break
        else:
          print("Invalid input. Enter a number between 0 to 6:")
      except ValueError:
        print("Invalid input. Enter a number between 0 to 6:")
    computerInput=random.randrange(0,7,1)
    print(f"Your input: {playerInput}")
    print(f"Computer input: {computerInput}")
    if playerInput==computerInput:
      print("\n")
      print("You bowled computer!")
      print(f"Computer score: {computerScore}")
      break
    else:
      computerScore=computerScore+computerInput
      print(f"Computer score: {computerScore}")
    ball=ball+1
    if ball==7:
      print(f"Over {over+1} completed.")
      ball=0
      over=over+1
    if computerScore>playerScore:
      break
else:
  # Player BATTING
  print("Your BATTING begins!")
  over=0
  ball=1
  while over<overs:
    print("\n")
    print(f"Ball {over}.{ball}:")
    print("Enter a number between 0 to 6:")
    while True:
      try:
        playerInput = int(input())
        if 0 <= playerInput <= 6:
          break
        else:
          print("Invalid input. Enter a number between 0 to 6:")
      except ValueError:
        print("Invalid input. Enter a number between 0 to 6:")
    computerInput=random.randrange(0,7,1)
    print(f"Your input: {playerInput}")
    print(f"Computer input: {computerInput}")
    if playerInput==computerInput:
      print("\n")
      print("You got bowled :(")
      print(f"Your score: {playerScore}")
      break
    else:
      playerScore=playerScore+playerInput
      print(f"Your score: {playerScore}")
    ball=ball+1
    if ball==7:
      print(f"Over {over+1} completed.")
      ball=0
      over=over+1
    if computerScore<playerScore:
      break

print("\n")
if playerScore>computerScore:
  print("You defeated computer!!! Congo!")
elif playerScore<computerScore:
  print("Computer wins and you lose, you suck!")
else:
  print("It's a tie.")
print("\n")
print("------------------------------------------")
