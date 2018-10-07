#!/usr/bin/env python3.6

from typing import List


def fib(n: int) -> List[int]:
    numbers = []

    current, nxt = 0, 1
    while len(numbers) < n:
        current, nxt = nxt, current + nxt
        numbers.append(current)

    return numbers


print(fib(10))
