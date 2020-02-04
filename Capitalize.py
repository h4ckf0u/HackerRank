#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    result = []
    for i in s.split(' '):
        result.append(i.capitalize())
    result = ' '.join(result)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    print(result)
    fptr.write(result + '\n')

    fptr.close()
