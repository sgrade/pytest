# A. Make a triangle!

arr = list(map(int, input().split()))
arr.sort()

# Editorial - https://codeforces.com/blog/entry/62455
print(max(0, arr[2] - (arr[0] + arr[1]) + 1))
