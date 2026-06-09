inventory = [
    {"name": "Sugar", "price": 130, "quantity": 10},
    {"name": "Salt", "price": 30, "quantity": 10},
]


def restock_product(inventory, item, qty):
    for inv in inventory:
        if item.lower() == inv["name"].lower():
            inv["quantity"] += qty
            return inv


print(restock_product(inventory, "Sugar", 50))
