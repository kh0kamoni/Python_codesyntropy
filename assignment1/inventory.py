# Define item names, quantities, and prices
item_names = ['Laptop', 'Keyboard', 'Mouse', 'Headphone', 'CPU', 'Monitor']
item_quantities = [10, 25, 25, 50, 20, 20]
items_prices = [50000, 1200, 1000, 1500, 48000, 18000]

# Display inventory with specific options
def display_items():
    print("\nItems [Quantities]\n")
    for i, j in zip(item_names, item_quantities):
        print(f"{i} {[j]}")

def payment(cart_items, cart_quantities):
    costs = 0 
    for itm in cart_items:
        costs += cart_quantities[cart_items.index(itm)] * items_prices[item_names.index(itm)]
    print(f"Total cost: BDT {costs:.2f} taka.")

    phone_number = input("Enter your phone number: ")
    pin = int(input("Enter your pin: "))
    print("Payment successful.")

    # Reduce quantities from the main inventory
    for item, quantity in zip(cart_items, cart_quantities):
        item_index = item_names.index(item)
        item_quantities[item_index] -= quantity
    print("Inventory updated.")

# Main menu
while True:
    # Display main menu
    print("\n1. View Items\n2. Add Item\n3. Remove Item\n4. Update item\n5. Manage Cart\n6. Exit")

    # Choose option
    option = int(input("What do you want to do?: "))

    # Decision make
    if option == 1:
        display_items()
    elif option == 2:
        # Code for adding new items to the inventory
        new_item = input("Item name: ")
        new_item_quantity = int(input("Quantity: "))
        new_item_price = int(input("Price: "))

        # Add new item to existing list
        item_names.append(new_item)
        item_quantities.append(new_item_quantity)
        items_prices.append(new_item_price)
        print("Successfully added item to the list.")

        # Display updated list
        print("\n\nUpdated list\n")
        display_items()
    elif option == 3:
        # Code for removing items from the inventory
        removed_item = input("Item name: ")

        if removed_item in item_names:
            rmvd_index = item_names.index(removed_item)

            # Remove name and quantity of the item
            item_names.pop(rmvd_index)
            item_quantities.pop(rmvd_index)

            # Display updated list
            print(f"Successfully removed item {removed_item} from the list.\n")
            print("Updated list\n")
            display_items()
        else:
            print("Error: item not found.")
    elif option == 4:
        # Code for updating item quantities in the inventory
        updated_item = input("Item name: ")

        # Item validity check
        if updated_item in item_names:
            updated_index = item_names.index(updated_item)

            # Update item quantities
            new_quantity = int(input("New quantity: "))
            item_quantities[updated_index] = new_quantity

            # Print updated list
            print("Item quantity successfully updated.\n")
            print("Updated list\n")
            display_items()
        else:
            print("Error: Invalid item.")
    elif option == 5:
        # Create empty list
        cart_items = []
        cart_quantities = []

        while True:
            print("\n1. View Cart\n2. Add to Cart\n3. Checkout\n4. Back to Main Menu")
            cart_option = int(input("Choose option: "))
            if cart_option == 1:
                print("\nCart Items [Quantities]\n")
                for k, l in zip(cart_items, cart_quantities):
                    print(f"{k} [{l}]")
            elif cart_option == 2:
                answer = "yes"
                while answer == "yes":
                    display_items()
                    print("\n")
                    added_cart_item = input("Item name: ")

                    # Item validation check
                    if added_cart_item in item_names:
                        added_cart_index = item_names.index(added_cart_item)
                        added_cart_quantity = int(input("Quantity: "))
                        if added_cart_quantity < item_quantities[added_cart_index]:
                            cart_items.append(added_cart_item)
                            cart_quantities.append(added_cart_quantity)
                            print(f"{added_cart_quantity} {added_cart_item} added to the cart.")
                            answer = input("Add another item to the cart? (yes/no): ")
                        else:
                            print("Insufficient quantity.")
                    else:
                        print("Error: Invalid item.")
            elif cart_option == 3:
                payment(cart_items, cart_quantities)
                break
            elif cart_option == 4:
                break
    elif option == 6:
        print("Thanks for shopping with us.")
        break
    else:
        print("Invalid option.")
