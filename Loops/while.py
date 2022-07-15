#demo while loops

#while loop as for loop
num = 1
while num <= 11:
    print(num)
    num += 1


#while loop on user input
msg = input("What's the secret code?: ")

while msg != 'Logan Roy':
    print("Incorrect, than answer is Logan Roy. Try again")
    msg = input("What's the secret code?: ")
print('Correct')
