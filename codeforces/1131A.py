# A. Sea Battle

w1, h1, w2, h2 = map(int, input().split())

# first rectangle: bottom, left and right, bottom corners
ans = w1 + h1 * 2 + 2

# second rectangle: top, left and right, top corners
ans += w2 + h2 * 2 + 2

# top not covered by the second
ans += max(0, w1 - w2)

print(ans)
