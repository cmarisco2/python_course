print("...rock...")
print("...paper...")
print("...scissors...")
print("(enter Player 1's choice): ")
firstChoice = input();
print("(enter Player 2's choice): ")
secondChoice = input();
print("Shoot!")

if firstChoice == secondChoice:
    print('Tie!')
else: 
    if firstChoice == 'rock':
        if secondChoice == 'paper':
            print('player2 wins')
        else:
            print('player1 wins')
    elif firstChoice == 'paper':
        if secondChoice == 'scissors':
            print('player2 wins')
        else:
            print('player1 wins')
    else:
        if secondChoice == 'rock':
            print('player2 wins')
        else:
            print('player1 wins')



