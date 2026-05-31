# function that returns the average number of passengers per trip,
# rounded to 1 decimal place.
trips = [
    {"route_name": "A", "passengers": 10, "fare_paid": 500},
    {"route_name": "B", "passengers": 8, "fare_paid": 400},
]


def get_avg_passengers(data):
    """Calculates total passengers and the average passengers per trip"""
    if not data:
        print("no data found")
        return
    total_passengers = 0

    for trip in data:
        route = trip["route_name"]
        passengers = trip["passengers"]
        total_passengers += passengers
        print(f"passengers in {route}:{passengers}")
    avg_passengers = total_passengers / len(trips)
    print(f"average passengers:{avg_passengers}")


try:
    get_avg_passengers(trips)
except Exception as e:
    print(f"An error has occured{e}")
