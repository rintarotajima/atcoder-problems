# 問題文
# N個の整数A₁、A₂、・・・ANの中に、整数Xが含まれるかを判定するプログラムを作成しろ。

# 入力
# N X
# A₁、A₂、・・・AN

N,X = map(int, input().split())
A = list(map(int, input().split()))
Answer = False

for i in range(N):
    if A[i] == X:
            Answer = True

if Answer == True:
      print("Yes")
else:
      print("No")