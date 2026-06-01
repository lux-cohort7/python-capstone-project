routes = [{'name':'CBD to Westlands','distance_km':5,'base_fare':50}]

def list_route():
    for index, route in enumerate(routes, start=1):
        print(f"{index}. {route['name']} | {route['distance_km']} KM | KES {route['base_fare']}")

list_route()
