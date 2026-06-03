routes = [{'name':'CBD to Westlands','distance_km':5,'base_fare':50},{'name':'CBD to Karen','distance_km':15,'base_fare':100}]

def get_short_routes(routes, max_km):
    short_routes = []
    for route in routes:
        if route['distance_km'] <= max_km:
            short_routes.append(route)
    return short_routes

print(get_short_routes(routes,10))
