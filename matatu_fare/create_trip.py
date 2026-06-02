def create_trip (route_name,passengers,fare_paid,):
    # Functio to create a new trip
    return{
        "route_name": route_name,
        "passengers": passengers,
        "fare_paid": fare_paid
    }

print(create_trip('CBD to Westlands', 12, 600))
