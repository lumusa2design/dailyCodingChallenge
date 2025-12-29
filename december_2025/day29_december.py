"""Takeoff Fuel

Given the numbers of gallons of fuel currently in your airplane, and the required number of liters of fuel to reach your destination, determine how many additional gallons of fuel you should add.

    1 gallon equals 3.78541 liters.
    If the airplane already has enough fuel, return 0.
    You can only add whole gallons.
    Do not include decimals in the return number.

"""
def fuel_to_add(current_gallons, required_liters):
    liters_in_current = current_gallons * 3.78541
    if liters_in_current >= required_liters:
        return 0
    additional_liters_needed = required_liters - liters_in_current
    additional_gallons_needed = additional_liters_needed / 3.78541
    return int(-(-additional_gallons_needed // 1)) 