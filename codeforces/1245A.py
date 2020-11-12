# A. Good ol' Numbers Coloring

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for _ in range(int(input())):
    a, b = map(int, input().split())
    # Editorial - https://codeforces.com/blog/entry/71080
    if gcd(a, b) == 1:
        print("Finite")
    else:
        print("Infinite")
