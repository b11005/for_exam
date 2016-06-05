#/usr/bin/env python 

import time, sys

def cul(x):
    if x <= 2:
        return 1
    else:
        return cul(x-1) + cul(x-2)


def cul2(x):
    if x<=2:
        return 1
    result = 0
    while x>0:
        result +=x
        x-=1
    return result


def cul25(n):
        if n <= 2:
            return 1
        else:
            x = y = 1
            for i in range(2, n):
                z = x + y
                x = y
                y = z
            return z


def cul3(x, y):
    if len(x) != 32 or len(y) !=32:
        return False
    else:
        return x + y


def main(args):
    n = int(args[0])
    print (cul(10))
    print (cul2(50))
    print cul25(50)
    print cul25(n)
    #print cul3(00123456789012345678901234567890L, 00987654321098765432109876543210L)
    #x = int(00123456789012345678901234567890)
    #y = int(00987654321098765432109876543210)
    

if __name__ == '__main__':
    main(sys.argv[1:])
