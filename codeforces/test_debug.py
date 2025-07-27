#!/usr/bin/env python3

# Simple competitive programming template
import sys
from collections import defaultdict, deque, Counter
import math
import heapq

def main():
    # Read input
    n = int(input())
    arr = list(map(int, input().split()))

    # Simple processing
    print(f"Array size: {n}")
    print(f"Array sum: {sum(arr)}")
    print(f"Array max: {max(arr)}")

if __name__ == "__main__":
    main()
