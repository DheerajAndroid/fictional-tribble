def battery_life(capacity, drain):
    """Return estimated battery life in hours from mAh and mAh/hour."""
    if (isinstance(capacity, bool) or isinstance(drain, bool)
            or not isinstance(capacity, (int, float))
            or not isinstance(drain, (int, float))):
        return "Invalid value: capacity and drain must be numbers"
    if capacity < 0:
        return "Invalid value: capacity must be zero or greater"
    if drain <= 0:
        return "Invalid value: drain must be greater than zero"

    return capacity / drain


if __name__ == "__main__":
    print(battery_life(5000, 500))  # 10.0 hours
