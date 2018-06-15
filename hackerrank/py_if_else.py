#!/bin/python3

# https://www.hackerrank.com/challenges/py-if-else/problem

import math
import os
import random
import re
import sys


def py_if_else(n):
    if N % 2 > 0:
        print('Weird')
    elif 2 <= N <= 5:
        print('Not Weird')
    elif 6 <= N <= 20:
        print('Weird')
    elif N >= 20:
        print('Not Weird')


if __name__ == '__main__':
    N = int(input())
    py_if_else(N)
