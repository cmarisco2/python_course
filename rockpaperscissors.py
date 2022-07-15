import random

com_select = random.randint(0, 2)
values = ['rock', 'paper', 'scissors']
com_choice = values[com_select]

print("...rock...")
print("...paper...")
print("...scissors...")
firstChoice = input("(enter Player 1's choice): ").lower()
secondChoice = com_choice
print(f"computer's choice is: {com_choice}")
print("Shoot!")

if firstChoice == secondChoice:
    print('Tie!')
else: 
    if firstChoice == 'rock':
        if secondChoice == 'paper':
            print('computer wins')
        else:
            print('player1 wins')
    elif firstChoice == 'paper':
        if secondChoice == 'scissors':
            print('computer wins')
        else:
            print('player1 wins')
    else:
        if secondChoice == 'rock':
            print('computer wins')
        else:
            print('player1 wins')



