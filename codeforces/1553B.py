# B. Reverse String
 
for _ in range(int(input())):
    s = input()
    t = input()

    # Idea from https://codeforces.com/contest/1553/submission/123300909

    for i in range(len(s)):
        x = s[:i] + s[i::-1]
        if t in x:
            print("YES")
            break
    else:
        print("NO")
