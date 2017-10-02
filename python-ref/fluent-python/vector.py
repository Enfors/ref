#!/usr/bin/env python3

"Based on Example 1-2 in Fluent Python."

from math import hypot

from demo import headline

class Vector:
    "Implements a simple vector."

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)

    def __abs__(self):
        ""
        return hypot(self.x, self.y)

    def __bool__(self):
        "Return True or False as appropriate."
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


def demo():
    "Demonstrate the Vector class."

    vector = Vector(2, 4)

    print(headline("General"))
    print("vector:", vector)
    print("vector * 3:", vector * 3)
    print("bool(vector):", bool(vector))
    print("bool(Vector(0, 0)):", bool(Vector(0, 0)))

if __name__ == "__main__":
    demo()
