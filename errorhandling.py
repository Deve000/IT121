"""
Deve J. Rebuta
IT1R4

IT121: Simple Money Withdrawal System
"""

def system():
    bal = 70000
    
    while True:
        print('\n\nSimple Money Withdrawal System')
        print('\nMenu:')
        print("1. Withdraw")
        print('2. Check current balance')
        print('3. Exit system')
        choiceA = int(input('\n>> Choose a number (1-3): '))

        if choiceA == 1:
            print('\n\nChosen action: Withdraw')
            try:
                amt = int(input('>> Enter amount: '))

                if amt <= 0:
                    print('\nInvalid amount. Please enter a positive value.')
                    continue

                elif amt > bal:
                    print('\nError: Insufficient funds.')

                    while True:
                        print('\nMenu:')
                        print('1. Re-enter new amount')
                        print('2. Check current balance')
                        print('3. Exit system')
                        choiceB = int(input('\n>> Choose a number (1-3): '))

                        if choiceB == 1:
                            amt = int(input('>> Enter amount: '))
                            bal -= amt
                            print(f'\nWithdrawn successfully. Current balance: {bal}')
                            break
                        elif choiceB == 2:
                            print(f'\nCurrent balance: {bal}')
                        elif choiceB == 3:
                            print('\nExiting system...')
                            return
                        else:
                            print('\nInvalid choice. Please choose from numbers 1-3.')
                    continue

                else:
                    bal -= amt
                    print(f'\nWithdrawn successfully. Current balance: {bal}')

            except ValueError:
                print('\nInvalid choice. Please choose form number 1-3.')

        elif choiceA == 2:
            print('\n\nChosen action: Check current balance')
            print(f'>> Current balance: {bal}')

        elif choiceA == 3:
            print('\n\nChosen action: Exit system')
            print('>> Exiting system...')
            break

        else:
            print('\n>> Invalid choice. Please choose from numbers 1-3.')

system()
