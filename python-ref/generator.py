#!/usr/bin/env python3


def fib():
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt
        yield current

# You can't just call fib() like a normal function, because it's not.
# It's a generator, so it works more like a list, or iterable.


for item in fib():
    print(item, end=", ")
    if item > 1000:
        break

print("\nDone")
