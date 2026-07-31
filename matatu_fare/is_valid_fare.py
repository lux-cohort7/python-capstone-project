def is_valid_fare(fare):
    """Return True if fare is a positive number, else False"""
    return fare > 0

if __name__ == "__main__":
    print(is_valid_fare(50))   # Expected: True
    print(is_valid_fare(-10))  # Expected: False
    print(is_valid_fare(0))    # Expected: False