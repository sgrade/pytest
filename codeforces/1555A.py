# A. PizzaForces

for _ in range(int(input())):
    n = int(input())

    # Solution is based on https://codeforces.com/contest/1555/submission/124369094

    ans = max(6, (n + 1)) // 2 * 5
    print(ans)
