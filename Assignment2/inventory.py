def load_inventory():
    try:
        with open('inventory_data.txt', 'r') as file:
            lines = file.readlines()
            inventory_data = {}
            for line in lines:
                product_id, name, price, quantity = line.strip().split(',')
                inventory_data[product_id] = {'name': name, 'price': float(price), 'quantity': int(quantity)}
            return inventory_data
    except FileNotFoundError:
        return {}

def save_inventory(inventory_data):
    with open('inventory_data.txt', 'w') as file:
        for product_id, details in inventory_data.items():
            file.write(f"{product_id},{details['name']},{details['price']},{details['quantity']}\n")

def add_product(product_id, name, price, quantity, inventory_data):
    if product_id not in inventory_data:
        inventory_data[product_id] = {'name': name, 'price': price, 'quantity': quantity}
    else:
        inventory_data[product_id]['quantity'] += quantity

def update_stock(product_id, quantity_change, inventory_data):
    if product_id in inventory_data:
        inventory_data[product_id]['quantity'] += quantity_change
