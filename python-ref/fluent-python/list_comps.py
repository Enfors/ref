#!/usr/bin/env python3

"Some examples from chapter 2."

from demo import headline

print(headline("Simple list comprehensions"))
symbols = "$©£←¤"
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

print(headline("Cartesian products - combining lists"))
colors = ["black", "white"]
sizes = list("SML")
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

# See also french_deck.py for further example.
