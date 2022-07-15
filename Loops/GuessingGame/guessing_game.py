# demo while loop and conditionals with an ongoing game:

from random import randint

random_number = randint(1, 10)

# Handle user guesses
#   if they guess correct, tell them they won
#   otherwise, tell them if they are too high or too low

# Bonus - let player guess again if they want

end_game = False

user_guess = None

while user_guess != random_number and not end_game:
    user_guess = input("Pick a number between 1 and 10: ")
    user_guess = int(user_guess)

    if user_guess == random_number:
        print("You guessed correctly!")
        continue_game = input("Do you wish to continue? Yes/No?: ").lower()
        if continue_game[0] == 'n':
            end_game = True
        else:
            random_number = randint(1, 10)
    elif user_guess < random_number:
        print("Sorry, your number is too low!")
    else:
        print("Sorry, your number is too high")
