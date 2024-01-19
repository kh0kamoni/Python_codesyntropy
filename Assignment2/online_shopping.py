import inventory
import shopping_cart
import payment

inventory_data = inventory.load_inventory()
cart_data = {}

while True:
    print("\n1. View Product Inventory")
    print("2. Add Product to Cart")
    print("3. View Cart")
    print("4. Proceed to Checkout")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Product Inventory:")
        for product_id, details in inventory_data.items():
            print(f"{product_id}: {details['name']} - ${details['price']} (Stock: {details['quantity']})")

    elif choice == '2':
        try:
            product_id = input("Enter Product ID: ")
            quantity = int(input("Enter Quantity: "))
            if product_id in inventory_data and quantity <= inventory_data[product_id]['quantity']:
                shopping_cart.add_to_cart(product_id, quantity, cart_data)
                print(f"{quantity} {inventory_data[product_id]['name']} added to the cart.")
            else:
                print("Invalid Product ID or insufficient stock.")
        except ValueError:
            print("Invalid input. Please enter a valid quantity.")

    elif choice == '3':
        if cart_data:
            print("Shopping Cart:")
            shopping_cart.view_cart(cart_data, inventory_data)
        else:
            print("Shopping Cart is empty.")

    elif choice == '4':
        if cart_data:
            total_amount = shopping_cart.checkout(cart_data, inventory_data)
            print(f"Total Amount: ${total_amount}")
            payment.process_payment(total_amount)
            inventory.save_inventory(inventory_data)
            cart_data = {}
        else:
            print("Shopping Cart is empty. Add items before proceeding to checkout.")

    elif choice == '5':
        break

    else:
        print("Invalid choice. Please enter a valid option.")
