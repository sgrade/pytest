#  B. The Great Hero

for _ in range(int(input())):
    A, B, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = False

    for i in range(n):
        fights = (b[i] + A - 1) // A
        B -= fights * a[i]

    if B + max(a) > 0:
        ans = True

    print("YES" if ans else "NO")
