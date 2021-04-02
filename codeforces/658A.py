# A. Bear and Reverse Radewoosh

n, c = map(int, input().split())
p = list(map(int, input().split()))
t = list(map(int, input().split()))

score_limak = 0
score_radewoosh = 0
time_limak = 0
time_radewoosh = 0

for i in range(n):
    time_limak += t[i]
    score_limak += max(0, p[i] - c * time_limak)

    time_radewoosh += t[n-i-1]
    score_radewoosh += max(0, p[n-i-1] - c * time_radewoosh)

if score_limak > score_radewoosh:
    print("Limak")
elif score_radewoosh > score_limak:
    print("Radewoosh")
else:
    print("Tie")
