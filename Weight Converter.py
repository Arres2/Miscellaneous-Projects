def weight_converter():
    weight = input('How much do you Weight? ')
    define = input("Is that pounds (P) or Kilograms (K)?")
    weight_kg = int(weight) / 0.45
    weight_lbs = int(weight) * 0.45
    if define.upper() == 'P':
        name = input('What is your name? ')
        msg = f'{name} you weight {weight_lbs} in kilograms'
        print(msg)
    elif define.upper() == 'K':
        name = input('What is your name? ')
        msg = f'{name} you weight {weight_kg} in pounds'
        print(msg)
    else:
        print(f'Invalid value')
        define


weight_converter()