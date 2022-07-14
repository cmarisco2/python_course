# ask for age
age = input("How old are you?: ")

if age:
    age = int(age)
    # 18-21 wristband
    if age >= 18 and age < 21:
        print("Enter but need a wristband")
    # 21+ normal entry
    elif age >= 21:
        print("You are good to go, drink away!")
    # too young
    else:
        print("Too young kiddo!")
else:
    print("Please enter an age")

