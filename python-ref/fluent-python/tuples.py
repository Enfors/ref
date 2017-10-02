#!/usr/bin/env python3

"Examples of tuples from chapter 2."

from collections import namedtuple

from demo import headline

print(headline("Tuples unpacking"))
lax_coorinates = (33.9425, 118.408056)
city, year, pop, chg, area = ("Tokyo", 2003, 32450, 0.66, 8014)
traveler_ids = [("USA", "31195855"), ("BRA", "CE342567"),
                ("ESP", "XDA205856")]
for passport in sorted(traveler_ids):
    print("%s/%s" % passport)

# Now we just want the country. Assign the other one to dummy var.
for country, _ in traveler_ids:
    print(country)

print(headline("Using * to grab excess items"))
a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(3)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)

# * can only be in one place.
a, *body, c, d = range(5)
print(a, body, c, d)

print(headline("Named tuples"))
City = namedtuple("City", "name country population coordinates")
tokyo = City("Tokyo", "JP", 36.933, (35.689722, 139.691667))
print("tokyo:", tokyo)
print("tokyo.population:", tokyo.population)
print("tokyo.coordinates:", tokyo.coordinates)
print("tokyo[1]:", tokyo[1])
print("City:", City)
print("City._fields:", City._fields)
