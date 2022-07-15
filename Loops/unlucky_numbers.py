
#loop through numbers 1-20 (inclusive)
#nums 4 || 13 print unlucky
#else if even -> print even
#or  if odd -> print odd

for num in range(1,21):
    if num == 4 or num == 13:
        state = "unlucky"
    elif num % 2 == 1:
        state = "Odd"
    else:
        state = "Even"
    print(f"{num}: {state}")