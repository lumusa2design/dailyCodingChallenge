"""

Given a weight in pounds as a number, return the string "(lbs) pounds equals (kgs) kilograms.".

    Replace "(lbs)" with the input number.
    Replace "(kgs)" with the input converted to kilograms, rounded to two decimals and always include two decimal places in the value.
    1 pound equals 0.453592 kilograms.
    If the input is 1, use "pound" instead of "pounds".
    If the converted value is 1, use "kilogram" instead of "kilograms".

"""

def convert_to_kgs(lbs):
    kgs = round(lbs * 0.453592, 2)
    lbs_unit = "pound" if lbs == 1 else "pounds"
    kgs_unit = "kilogram" if kgs == 1 else "kilograms"
    return f"{lbs} {lbs_unit} equals {kgs:.2f} {kgs_unit}."

