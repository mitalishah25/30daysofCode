# Problem Statement: https://www.hackerrank.com/challenges/30-binary-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys


def countOnes(n):

    con_1s = 0 # count for consecutive 1s
    max_con_1s = 0 # maximum consecutives 1s
    
    # convert decimal to binary
    while n > 0:
        remainder = n % 2
        if remainder == 1:
            con_1s += 1
            if con_1s > max_con_1s:
                max_con_1s = con_1s
        else:
            con_1s = 0
        n = n // 2

    return max_con_1s

if __name__ == '__main__':
    n = int(input())
    print(countOnes(n))
