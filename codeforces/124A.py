# A. The number of positions

n, a, b = map(int, input().split())
# Solution from https://codeforces.com/blog/entry/3047?#comment-226570
print(min(n - a, b + 1))
