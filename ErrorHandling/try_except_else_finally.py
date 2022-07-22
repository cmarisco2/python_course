# demo basic try except finally else

while True:
    try:
        num = int(input('Enter a number: '))
        print(f"you entered {num} good job")
    except TypeError as err:
        print('argument MUST be a STRING')
        print(err)
    except ValueError as err:
        print('must enter a NUMBER of type string')
        print(err)
    else:
        print('thinks for playing')
        break
    finally:
        print('This will always run')
