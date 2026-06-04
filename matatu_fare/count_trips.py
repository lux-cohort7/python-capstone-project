trips = [
    {"route_name": "A", "passengers": 10, "fare_paid": 500},
    {"route_name": "B", "passengers": 8, "fare_paid": 400},
]


def count_trips(trips):
    """Calculates total trips without using len()."""
    total_trips = 0

    for trip in trips:
        # Increment trip count manually
        total_trips += 1

    return total_trips


if __name__ == "__main__":
    # expected outcome: 2
    print(f"{'Metric':<20} | {'Value':>10}")
    print("-" * 40)
    print(f"{'Total Trips':<20} | {count_trips(trips):>10}")
    print("-" * 40)
