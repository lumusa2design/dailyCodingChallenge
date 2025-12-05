'''Miles to Kilometers

Given a distance in miles as a number, return the equivalent distance in kilometers.

    The input will always be a non-negative number.
    1 mile equals 1.60934 kilometers.
    Round the result to two decimal places.
    Remove unnecessary trailing zeros from the rounded result.'''


def convertToKm(miles):
  miles = round(miles * 1.60934, 2)
  if miles.is_integer():
    miles = int(miles)
  return miles
