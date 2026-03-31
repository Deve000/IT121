"""
Deve J. Rebuta
IT1R4
IT121

PIT 1: Simple Calculator Program
"""

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return '\nCannot divide by zero, please choose another number.\n'
    else:
        return num1 / num2

def calculator():
    while True:
        print('\n---Simple Calculator Program---\n\n')
        print('Choose an operation:')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Exit')

        choice = int(input('\nEnter your choice (1-5): '))

        if choice == 5:
            print('\nExiting program, goodbye!\n')
            break

        if choice == 1 or choice == 2 or choice == 3 or choice == 4:
            num1 = float(input('\nEnter first number: '))
            num2 = float(input('Enter second number: '))

            if choice == 1:
                result = add(num1, num2)
            elif choice == 2:
                result = subtract(num1, num2)
            elif choice == 3:
                result = multiply(num1, num2)
            elif choice == 4:
                result = divide(num1, num2)

            print('\nResult: ', result)
        else:
            print('\nInvalid choice. Please select from 1-5.\n')

calculator()
