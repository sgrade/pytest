# A. Petya and Origami

n, k = map(int, input().split())
red = (n * 2 + k - 1) // k
green = (n * 5 + k - 1) // k
blue = (n * 8 + k - 1) // k
print(red + green + blue)
