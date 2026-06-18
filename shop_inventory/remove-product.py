def remove_product(inventory, name):
    """Remove a product by name from the inventory list."""
    return [product for product in inventory if product['name'] != name]


if __name__ == "__main__":
    inventory = [
        {'name': 'Sugar', 'price': 130, 'quantity': 100},
        {'name': 'Salt', 'price': 50, 'quantity': 200}
    ]

    print(remove_product(inventory, 'Sugar'))
