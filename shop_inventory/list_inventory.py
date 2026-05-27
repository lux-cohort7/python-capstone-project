def print_products(products):
  for i, product in enumerate(products):
    name, price, quantity = product
    print(f"{i+1}. {name} | Price: KES {price} | Qty: {quantity}")
products_list = [
    ("Sugar", 130, 100),
    ("Milk", 55, 50),
    ("Bread", 60, 200)
]

print_products(products_list)
