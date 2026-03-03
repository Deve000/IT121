"""
Deve Rebuta
IT1R4

IT121: Simple Login System Program
"""

correct_pass = 'ustp123'

username = input('\nEnter username: ')
user_pass = input('Enter password: ')

if user_pass == correct_pass:
    print('\n\nLogged in.\n')
else:
    print('\n\nAccess denied.\n')