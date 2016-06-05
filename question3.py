#!/usr/bin/env python
#coding: utf-8

import sys

def fib(n):
    if n <= 2:
        return 1
    else:
        x = y = 1
        for i in range(2,n):
            z = x + y
            x = y
            y = z
        return z

def main(args):
    n = int(args[0])
    print fib(n)


if __name__ == "__main__":
    main(sys.argv[1:])
