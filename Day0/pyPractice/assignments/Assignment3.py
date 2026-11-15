def km_to_miles(km):
    """Convert kilometers to miles, rounded to two decimal places."""
    return round(km / 1.609344, 2)


def miles_to_km(mi):
    """Convert miles to kilometers, rounded to two decimal places."""
    return round(mi * 1.609344, 2)


if __name__ == "__main__":
    print(km_to_miles(10))  # 6.21
    print(miles_to_km(10))  # 16.09
