from inventory import update_stock

def add_to_cart(product_id, quantity, cart_data):
    if product_id not in cart_data:
        cart_data[product_id] = {'quantity': quantity}
    else:
        cart_data[product_id]['quantity'] += quantity

def view_cart(cart_data, inventory_data):
    total_amount = 0
    for product_id, item in cart_data.items():
        name = inventory_data[product_id]['name']
        price = inventory_data[product_id]['price']
        quantity = item['quantity']
        total_amount += price * quantity
        print(f"Product: {name}, Quantity: {quantity}, Price: ${price * quantity}")
    print(f"Total Amount: ${total_amount}")

def checkout(cart_data, inventory_data):
    total_amount = 0
    for product_id, item in cart_data.items():
        price = inventory_data[product_id]['price']
        total_amount += price * item['quantity']
        update_stock(product_id, -item['quantity'], inventory_data)
    return total_amount
