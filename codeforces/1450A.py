#

for _ in range(int(input())):
    n = int(input())
    s = input()
    cnt = s.count('r')
    ans = cnt * 'r' + ''.join([x for x in s if x != 'r'])
    print(ans)
