# B. Putting Plates

for _ in range(int(input())):
    h, w = map(int, input().split())

    ans = list()

    for i in range(h):

        s = ""
        
        if i % 2 == 0:

            if i == 0 or i == h-1:
                s = '10' * (w//2) + '1' * (w % 2)
            else:
                s = '1' + '0' * (w - 2) + '1'

        else:
            if i == h-1 and w > 4:
                s_lst = list()
                s_lst.append('00')
                for j in range(w - 4):
                    if j % 2 == 0:
                        s_lst.append('1')
                    else:
                        s_lst.append('0')
                s_lst.append('00')
                s = ''.join(s_lst)
            else:
                s = '0' * w
            
        ans.append(s)

    print('\n'.join(ans))
    print()
