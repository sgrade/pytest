# A. Tricky Alchemy

a, b = map(int, input().split())
x, y, z = map(int, input().split())

required_a = x * 2 + y
required_b = y + z * 3
print(max(0, required_a - a) + max(0, required_b - b))
