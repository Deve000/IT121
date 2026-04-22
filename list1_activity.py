"""
Rebuta, Deve Sophia J.
IT1R4

Lists (1): Contact Manager
"""

contacts = []

while True:
    print('\n\nContact Manager System')
    print('\n1. Add contact')
    print('2. Remove contact')
    print('3. Exit')
    choice = int(input('\nEnter choice (1-3): '))

    if choice == 1:
        add_name = input('\nEnter contact name: ')
        add_num = input('Enter contact number: ')
        new_contact = add_name, add_num
        contacts.extend(new_contact)
        print(f'\n\nNew contact {add_name} added successfully.\n')
        print("--------------------------------------")
        print('\nContacts:\n', contacts,'\n')
        print("--------------------------------------")

    elif choice == 2:
        remove = input('\nEnter contact name to remove: ')
        print("\n--------------------------------------")
        print('\nContacts:\n', contacts,'\n')
        print("--------------------------------------")
        
        if remove in contacts:
            contacts.remove(remove)
            print(f'\nContact {remove} removed successfully.\n')
        else:
            print('\nContact not found.\n\n')

    elif choice == 3:
        print('\n\nExiting system...')
        break

    else:
        print('\nInvalid choice, try again.\n\n')
