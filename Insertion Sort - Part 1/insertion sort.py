#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    temp = arr[len(arr) - 1]
    for i in range(len(arr)-1, -1, -1):
        if i >= 1 and arr[i-1] > temp:
            arr[i] = arr[i-1]
            print(' '.join(list(map(str, arr))))
        else:
            arr[i] = temp
            print(' '.join(list(map(str, arr))))
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
