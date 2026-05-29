def is_valid_age(age):
    """
    Returns True if the age is a number between 0 and 120 (inclusive).
    Returns False otherwise.
    """
    if not isinstance(age, (int, float)):
        return False
    
    if age >= 0 and age <= 120:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_valid_age(35))
    print(is_valid_age(-1))
    print(is_valid_age(150))
    print(is_valid_age(72))
    print(is_valid_age(121))
    print(is_valid_age("25"))
    print(is_valid_age(25.5))
