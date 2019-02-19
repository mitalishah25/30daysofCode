#!/bin/python3

import math
import os
import random
import re
import sys

def hourglass(m,n):
    sum = 0
    for i in range(m, m+3):
        for j in range(n, n+3):
            if i != m+1:
                sum += arr[i][j]
    sum += arr[m+1][n+1]
    return sum
            

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    rows = len(arr)
    cols = len(arr[0])
    m = 0
    n = 0
    sum_arr = []
    while m<=rows and n<=cols:
        sum = hourglass(m,n)
        sum_arr.append(sum)
        n += 1
        if n > cols-3:
            n = 0
            m += 1
            if m > rows-3:
                break
    print(max(sum_arr))
