def get_daily_summary(trips):
    return {
        "total_trips": len(trips),
        "total_passengers": sum(trip["passengers"] for trip in trips),
        "total_revenue": sum(trip["fare_paid"] for trip in trips)
    }

trips = [{'route_name':'A','passengers':10,'fare_paid':500},{'route_name':'B','passengers':8,'fare_paid':400}]
print(get_daily_summary(trips))
