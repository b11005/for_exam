#!/usr/bin/env python

import sys
import time

def f(n):
    start = time.time()
    print 'f(n)'
    #print 100000*n
    print time.time() - start


def g(n):
    start = time.time()
    print 'g(n)'
    print (10*int(n))**3
    print time.time() - start


def h(n):
    start = time.time()
    print 'h(n)'
    print 2**int(n)
    print time.time() - start


def main(args):
    n = args[0]
    f(n)
    g(n)
    h(n)

if __name__ == '__main__':
    main(sys.argv[1:])
