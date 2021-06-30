# B. Planet Lapituletti

mirror = [0, 1, 5, 100, 100, 2, 100, 100, 8, 100]

def print_ans(hours, minutes):
    ans = str(hours).zfill(2) + ':' + str(minutes).zfill(2)
    print(ans)

for _ in range(int(input())):
    h, m = map(int, input().split())
    sh, sm = map(int, input().split(':'))

    # Key ideas are from https://codeforces.com/contest/1493/submission/110107120
    while True:
        mirror_h = mirror[sm%10] * 10 + mirror[sm//10]
        mirror_m = mirror[sh%10] * 10 + mirror[sh//10]
        if mirror_h < h and mirror_m < m:
            print_ans(sh, sm)
            break
        sm += 1
        if sm == m:
            sm = 0
            sh = (sh + 1) % h
