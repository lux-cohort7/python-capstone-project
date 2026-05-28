def get_best_trip(trips):  
    # initialize first trip as best
    best_trip = trips[0] 

    # iterate through list to get the highest revenue trip
    for trip in trips:
        if trip['fare_paid'] > best_trip['fare_paid']:
            best_trip = trip
    return best_trip
    