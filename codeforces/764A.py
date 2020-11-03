# A. Taymyr is calling you

n, m, z = map(int, input().split())

ans = 0

if z >= n and z >= m:
    n_list = [n]
    m_list = [m]
    for _ in range(1, z // n):
        n_list.append(n_list[-1] + n)
    for _ in range(1, z // m):
        m_list.append(m_list[-1] + m)

    for el in m_list:
        if el in n_list:
            ans += 1

print(ans)


'''
# Better solution from the Editorial:
# https://codeforces.com/blog/entry/50205 

from math import gcd
 
n, m, z = map(int, input().split())
g = gcd(n, m)
lcm = n * m // g
print(z // lcm)
'''