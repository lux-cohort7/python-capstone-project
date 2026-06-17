def count_products(inventory):
    count = 0

    for product in inventory:
        count += 1

    return count


if __name__ == "__main__":
    inventory = [
        {"name": "Sugar", "price": 130, "quantity": 5},
        {"name": "Salt", "price": 50, "quantity": 200}
    ]

    print(count_products(inventory))
