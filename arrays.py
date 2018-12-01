import random
import re
import sys

def revarr(arr):
    revarr = []
    for i in range(len(arr)-1, -1, -1):
        revarr.append(arr[i])
    print(*revarr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    revarr(arr)