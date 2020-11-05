# A. Almost Prime

from math import sqrt


def all_distinct_prime_factors(n):
    st = set()
    if n == 0 or n == 1:
        return st
    else:
        while n % 2 == 0:
            st.add(2)
            n = n // 2
        for i in range(3, int(sqrt(n))+1, 2):
            while n % i == 0:
                st.add(i)
                n = n // i
        if n > 2:
            st.add(n)
    return st


n = int(input())
ans = 0
for i in range(1, n+1):
    if len(all_distinct_prime_factors(i)) == 2:
        ans += 1
print(ans)
