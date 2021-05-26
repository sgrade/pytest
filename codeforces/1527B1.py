# B1. Palindrome Game (easy version)

for _ in range(int(input())):
    n = int(input())
    s = input()

    zeroes = s.count('0')

    ab = ["ALICE", "BOB"]
    ans = ""

    if zeroes % 2 != 0:
        ans = ab[1] if zeroes == 1 else ab[0]
    else:
        ans = ab[1]
    
    print(ans)
