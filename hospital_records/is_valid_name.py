def is_valid_name(name):
    if isinstance(name, str) and name.strip() != "":
        return True
    return False


if __name__ == "__main__":
    print(is_valid_name("Moses Otieno"))
    print(is_valid_name(""))