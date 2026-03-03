x = 300

print('Find the closest number to {x}\n')

def closest_num():
    a = int(input('Enter your first number: '))
    b = int(input('Enter your second number: '))
    c = int(input('Enter your third number: '))

    if a == b == c:
        print(f'\nA is {a}, B is {b}, and C is {c} are all equal, therefore all numbers are closest to {x}')
    elif a >= b and a >= c:
        print(f'\nLetter A or {a} is the closest number to {x}')
    elif b >= a and b >= c:
        print(f'\nLetter B or {b} is the closest number to {x}')
    else:
        print(f'\nLetter C or {c} is the closest number to {x}')

closest_num()