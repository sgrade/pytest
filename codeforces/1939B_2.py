# B. Planet Lapituletti
# wrong answer 8th lines differ - expected: '50:00', found: '00:00'

from re import search


good = "012xx5xx8x"

# Python: Find first non-matching character
# https://stackoverflow.com/questions/19191287/python-find-first-non-matching-character
def check(begin, end):
    if 2 <= end < 5:
        end = 5
    match = search(r'[^x]', good[begin:end+1])
    if match:
        idx = match.start()
        return good[begin+idx]
    else:
        return '0'

def get_num_in_mirror(a, b):
    lst = [a, b]
    for i in range(2):
        if lst[i] == '2':
            lst[i] = '5'
        elif lst[i] == '5':
            lst[i] = '2'
    return int(lst[0] + lst[1])


for _ in range(int(input())):
    h, m = map(int, input().split())
    h -= 1
    m -= 1
    sh, sm = map(int, input().split(':'))

    ans = []
    
    ans.append(check(sh//10, m%10))
    if int(ans[0]) > sh//10:
        ans.append('0')
    else:
        ans.append(check(sh%10, h%10))
    h_ans = int(ans[0] + ans[1])
    # real clock
    if h < h_ans or h_ans < sh:
        h_ans = 0
        ans[0] = '0'
        ans[1] = '0'
        
    ans.append(':')
    
    # next hour starts from 0 minutes
    if h_ans == 0 or h_ans > sh:
        ans.append('0')
        ans.append('0')
    # minutes in the same hour as sh
    else:
        ans.append(check(sm//10, h%10))
        if int(ans[3]) > sm//10:
            ans.append('0')
        else:
            ans.append(check(sm%10, m%10))
        # real clock
        m_ans = int(ans[3] + ans[4])
        if m < m_ans or m_ans < sm:
            ans[3] = '0'
            ans[4] = '0'

    # Checking mirror
    h_ans_in_mirror = get_num_in_mirror(ans[4], ans[3])
    m_ans_in_mirror = get_num_in_mirror(ans[1], ans[0])
    if m < m_ans_in_mirror:
        ans[0] = '0'
        ans[1] = '0'
        h_ans_in_mirror = 101
    if h < h_ans_in_mirror:
        ans[3] = '0'
        ans[4] = '0'
    
    print(''.join(ans))
    