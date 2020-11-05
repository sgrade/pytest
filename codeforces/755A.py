# A. PolandBall and Hypothesis

def is_prime(x):
    if x == 0 or x == 1:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
    return True


n = int(input())
for i in range(1, 1001):
    if not is_prime(n * i + 1):
        print(i)
        break
