routes = [
    {"name": "CBD to Westlands", "distance_km": 5, "base_fare": 50},
    {"name": "CBD to Karen", "distance_km": 15, "base_fare": 100},
]


def remove_route(routes, name):
    """
    Removes the route matching the given name (case-insensitive).
    """
    for route in routes:
        if name.lower() == route["name"].lower():
            routes.remove(route)
            return routes  # Return the list after successful removal
    # Only print error if the loop finishes without finding a match
    print("Route does not exist, try again!")
    return routes


# Test the function
result = remove_route(routes, "CBD to Westlands")
print(result)
