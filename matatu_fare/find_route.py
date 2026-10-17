def find_route(routes, name):
    for route in routes:
        if route["name"] == name:
            return route

    return "Route not found"



