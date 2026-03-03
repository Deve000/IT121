print('\nUser Management System\n')

def menu():

    all_users = []

    while True:
        print('Menu:')
        print('1 - Show Users\n2 - Add User\n3 - Update User\n4 - Delete User\n5 - Exit')
        choice = int(input('\nChoose a number (1 to 5): '))
        
        if choice == 1:
            print('\nUsers:\n', all_users,'\n')
    
        elif choice == 2:
            add = input('\nAdd New User Name: ')
            all_users.append(add)
            print(f'\nNew user {add} added successfully.\n\n')

        elif choice == 3:
            update = input('\nWhich user do you want to update? ')
            if update in all_users:
                index = all_users.index(update)
                new_user = input('\nEnter new user name: ')
                all_users[index] = new_user
                print(f'\nUser {new_user} updated successfully.\n')
            else:
                print('\nUser name not found, try again.\n\n')

        elif choice == 4:
            remove = input('\nWhich user do you want to remove? ')
            if remove in all_users:
                all_users.remove(remove)
                print(f'\nUser {remove} successfully deleted.\n')
            else:
                print('\nUser name not found, try again.\n\n')
            
        elif choice == 5:
            print('\nExiting User Management Sytem Program. Goodbye!\n')
            quit()

        else:
            print('Invalid choice. Please choose a number from 1 to 5.')

menu()