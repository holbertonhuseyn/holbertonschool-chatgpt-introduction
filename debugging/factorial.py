#!/usr/bin/env python3
import sys

def factorial(n):
    try:
        n = int(n)
        if n < 0:
            return 0
        result = 1
        while n > 1:
            result = result * n
            n = n - 1
        return result
    except:
        return 1

if len(sys.argv) > 1:
    print(factorial(sys.argv[1]))
else:
    print(1)
