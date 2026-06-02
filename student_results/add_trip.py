def add_trip(trips, route_name, passengers, fare_paid):
    """
    Creates a trip dict and appends to trips list

    Parameters
    ----------
    route_name : stringSS
        name of route done
    passengers : int
        number of passangers on board.
    fare_paid : float
        sum of fare collected.

    Returns
    -------
    list
        updated list(trips) 
    """
    trip = {
        "route_name": route_name,
        "passengers": passengers,
        "fare_paid": fare_paid
        }
    trips.append(trip)
    return trips
