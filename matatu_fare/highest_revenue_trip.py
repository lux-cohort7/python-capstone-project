def get_best_trip(trips):  
    # initialize first trip as best
    best_trip = trips[0] 

    # iterate through list to get the highest revenue trip
    for trip in trips:
        if trip['fare_paid'] > best_trip['fare_paid']:
            best_trip = trip
    return best_trip
    

# add test
if __name__ == "__main__":
    trips = [{'route_name':'A','passengers':10,'fare_paid':500},{'route_name':'B','passengers':8,'fare_paid':1000}]
    print(get_best_trip(trips)['route_name'])