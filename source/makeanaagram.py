#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    removes = 0
    hashdict_a = dict()
    hashdict_b = dict()
    for letter in a:
        if letter in hashdict_a:
            hashdict_a[letter] += 1
        else:
            hashdict_a[letter] = 1
    for letter in b:
        if letter in hashdict_b:
            hashdict_b[letter] += 1
        else:
            hashdict_b[letter] = 1
            
    for letter in hashdict_a:
        if letter not in hashdict_b:
            removes += hashdict_a[letter]
            print(letter+" is not at dict b" + " and removes is: ", removes)
            
        else:
            if hashdict_a[letter] > hashdict_b[letter]:
                print("in A there are ", hashdict_a[letter] - hashdict_b[letter], "letters " + letter )
                hashdict_a[letter] = hashdict_a[letter] -           (hashdict_a[letter] - hashdict_b[letter])
                removes += hashdict_a[letter] - hashdict_b[letter]
            elif hashdict_a[letter] < hashdict_b[letter]:
                print("in B there are ", hashdict_b[letter] - hashdict_a[letter], "letters " + letter )
                hashdict_b[letter] = hashdict_b[letter] - (hashdict_b[letter] - hashdict_a[letter])
                removes += hashdict_b[letter] - hashdict_a[letter]
    for letter in hashdict_b:
        if letter not in hashdict_a:
            removes += hashdict_b[letter]
    return removes
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
