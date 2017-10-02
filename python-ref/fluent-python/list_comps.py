#!/usr/bin/env python3

"Some examples from chapter 2."

from demo import headline

print(headline("Simple list comprehensions"))
symbols = "$©£←¤"
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
