while True:
    try:
        age = int(input('What is your age?\n'))
        print(age)
        break
    except ValueError:
        print('Invalid value encountered')
