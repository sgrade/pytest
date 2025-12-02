import math


def gcd(a, b):
    """Greatest common divisor. Use math.gcd in Python 3.5+."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Least common multiple."""
    return a * b // math.gcd(a, b)


def is_prime(n):
    """Check if n is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def sieve_of_eratosthenes(n):
    """Return all primes up to n."""
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


def mod_pow(base, exp, mod):
    """Fast modular exponentiation: (base^exp) % mod."""
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = result * base % mod
        exp >>= 1
        base = base * base % mod
    return result


def mod_inverse(a, mod):
    """Modular inverse of a mod m (when mod is prime)."""
    return mod_pow(a, mod - 2, mod)


def count_digits(n):
    """Count number of digits in n."""
    if n == 0:
        return 1
    return int(math.log10(abs(n))) + 1

