# A. Contest Start

for _ in range(int(input())):
    n, x, t = map(int, input().split())

    ans = 0
    
    # Editorial - https://codeforces.com/blog/entry/91906
    
    if t >= x:
        # Participants from 1 to n - t/x
        dissatisfaction_for_one = min(n-1, t//x)
        participants_with_full_dissatisfaction = max(0, n - dissatisfaction_for_one)
        ans += dissatisfaction_for_one * participants_with_full_dissatisfaction
        
        # Rest
        # Ariphmetic progression with -1 for each nextx§
        first = max(0, dissatisfaction_for_one - 1)
        last = 0
        num_of_rest = max(0, n - participants_with_full_dissatisfaction)
        sm = (first + last) * num_of_rest // 2
        ans += sm

    print(ans)
