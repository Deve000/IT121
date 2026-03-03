def largest_num():
    a = int(input('Enter your first number: '))
    b = int(input('Enter your second number: '))
    c = int(input('Enter your third number: '))

    if a >= b and a >= c:
        print(f'\nLetter A is the largest number with a value of {a}')
    elif b >= a and b >= c:
        print(f'\nLetter B is the largest number with a value of {b}')
    else:
        print(f'\nLetter C is the largest number with a value of {c}')

largest_num()