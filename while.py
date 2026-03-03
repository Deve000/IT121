"""
Deve Rebuta
IT1R4

IT121: While Loop
"""

while True:
    user_pass = input('\nEnter password: ')

    if (any(ch.isalpha()for ch in user_pass) and (any(ch.isnumeric() for ch in user_pass))) :
        print('\nPassword accepted.\n')
        break
    else:
        print('\nInvalid pasword.Try again.\n')