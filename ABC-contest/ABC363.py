# B問題
# N人の人がおり、i人目(1<=i<=N)の現在の髪の長さはLiである。
# すべての人は1日経つごとに髪の長さが1ずつ増える。
# 髪の長さがT以上の人が初めてP人以上になるのは現在から何日後か出力してください。
# ただし、現在の時点ですでに髪の長さがT以上の人がP人以上いるときは0を出力してください。

N,T,P = map(int, input().split())
L = list(map(int, input().split()))

for i in range(T):
    count = 0
    for j in range(N):
        if L[j] + i>= T:
            count += 1
    if count >= P:
        print(i)
        break
