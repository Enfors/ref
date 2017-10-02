#!/usr/bin/env python3

import array

from demo import headline

"Some examples of generator expressions from chapter 2."

print(headline("General"))
symbols = "$©£←¤"
print(tuple(ord(symbol) for symbol in symbols))
print(array.array('I', (ord(symbol) for symbol in symbols)))
