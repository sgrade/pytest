# A. Display The Number

for _ in range(int(input())):
    n = int(input())

    # Editorial - https://codeforces.com/blog/entry/73467

    ans = ""
    if n >= 3 and n % 2 != 0:
        ans += '7'
        n -= 3
    ans += '1' * (n // 2)

    print(ans)
