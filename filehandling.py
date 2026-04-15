"""
Deve J. Rebuta
IT1R4

IT121: Simple Messaging Application
"""

try:
    f = open('message.txt', 'x')
    f.close()
    print("\n>> File 'message.txt' is created successfully.")
except FileExistsError:
    print("\n>> File 'message.txt' already exists.")

while True:
    print('\n\nSimple Messaging Application')
    print('\nMenu:')
    print('1. Send message')
    print('2. View all messages')
    print('3. Exit')
    choice = int(input('\n>> Choose a number (1-3): '))

    if choice == 1:
        print('\nSend Message')
        mssg = input('>> Enter your message: ')
        try:
            if mssg == '':
                print('\n>> Empty messages are unallowed.')
            else:
                f = open('message.txt', 'a')
                f.write(mssg + '\n')
                f.close()
        except Exception as e:
            print('\n>> Error: Message cannot be sent.', e)

    elif choice == 2:
        print('\nView All Messages\n')
        try:
            f = open('message.txt', 'r')
            mssg = f.read()
            f.close()
            print(mssg + '\n')
        except Exception as e:
            print('Error: Messages cannot be viewed', e)

    elif choice == 3:
        print('\nExit App')
        print('Exiting app...')
        break

    else:
        print('\nInvalid number, please choose from 1-3.')
