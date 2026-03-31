"""
Deve J. Rebuta
IT1R4
IT121

Midterm Laboratory: Shopping Cart Simulator Program
"""

class shop_cart:
    def __init__(self):
        self.cart = []

    def add_cart(self, item):
        self.cart.append(item)
        print(item, '\n\nItem added to cart.\n')

    def remove_cart(self, item):
        if item in self.cart:
            self.cart.remove(item)
            print(item, '\n\nItem removed from cart.\n')
        else:
            print(item, '\n\nItem not found in cart.\n')

    def view_cart(self):
        if len(self.cart) == 0:
            print('\nYour cart is empty.\n')
        else:
            print('\nItems in your cart:')
            for item in self.cart:
                print('-', item)

    def checkout(self):
        if len(self.cart) == 0:
            print('\nYour cart is empty. Cannot checkout.\n')
        else:
            print('\nChecking out the following items: ')
            for item in self.cart:
                print('-', item)
            print('\nThank you for shopping!\n')
            self.cart.clear()

def main():
    cart = shop_cart()

    while True:
        print('\n---Shopping Cart Simulator Program---')
        print('\nMenu:')
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")

        choice = int(input('\nEnter your choice (1-5): '))

        if choice == 1:
            item = input('\nEnter item to add: ')
            print('\nItem: ')
            cart.add_cart(item)

        elif choice == 2:
            item = input('\nEnter item to remove: ')
            print('\nItem:')
            cart.remove_cart(item)

        elif choice == 3:
            cart.view_cart()

        elif choice == 4:
            cart.checkout()

        elif choice == 5:
            print('\nExiting program, goodbye!\n')
            break

        else:
            print('\nInvalid choice. Please choose from 1 - 5.\n')

main()
