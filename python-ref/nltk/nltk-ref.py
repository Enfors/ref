#!/usr/bin/env python3

import nltk

text1 = "to be or not to be that is the question".split(" ")

# Frequency distribution (like bag of words, I think?)
fdist1 = nltk.FreqDist(text1)
print(fdist1)
print("== Most common words")
print(fdist1.most_common(4))
print("== Num occurances of 'to':")
print(fdist1["to"])
