#!/usr/bin/env python3

import multiprocessing
from multiprocessing.pool import Pool

"""
Example taken from async course on www.talkpython.fm.
"""


def do_math(a: int, b: int):
    print("%d + %d = %d" % (a, b, a + b))

print("You have %d processors." % multiprocessing.cpu_count())
pool = Pool(processes=4)
pool.apply_async(func=do_math, args=(0, 100))
pool.apply_async(func=do_math, args=(101, 200))
pool.apply_async(func=do_math, args=(201, 300))
pool.apply_async(func=do_math, args=(301, 400))

pool.close()
pool.join()
