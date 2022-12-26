#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    # Weird case
    if n % 2 != 0 or (n % 2 == 0 and n in range(6, 21)):
        print('Weird')
    # Not Weird case
    elif (n % 2 == 0 and n in range(2, 6)) or (n % 2 == 0 and n > 20):
        print('Not Weird')
