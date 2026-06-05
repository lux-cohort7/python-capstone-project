# Write a function that returns a dict: total_products, total_items (sum of quantities), total_value (sum of price*qty).
inventory = [
    {"name": "Sugar", "price": 100, "quantity": 10},
    {"name": "Salt", "price": 50, "quantity": 20},
]

summary = {"total_products": 0, "total_items": 0, "total_value": 0}


def get_inventory_summary(inventory):
    """Returns a dict with total_products, total_items, and total_value."""
    summary["total_products"] = len(inventory)
    for i in inventory:
        summary["total_items"] += i["quantity"]
        summary["total_value"] += i["quantity"] * i["price"]
    return summary


print(get_inventory_summary(inventory))
