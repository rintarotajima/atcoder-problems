# B問題

# 問題文
# xy平面上に、同一直線上にない3点 A(xA,yA)、B(xB,yB)、C(xC,yC)があります。三角形ABCが直角三角形であるかを判定してください。

# 制約
# -1000 <= xA,yA,xB,yB,xC,yC <= 1000
# ・3点 A,B,Cは同一直線上にない。
# ・入力はすべて整数

# 入力
# xA yA
# xB yB
# xC yC

# 出力
# 三角形ABCが直角三角形だったら"Yes"を、そうでなければ"No"を出力せよ。

# 模範解答
xA, yA = map(int, input().split())
xB, yB = map(int, input().split())
xC, yC = map(int, input().split())

AB2 = (xA - xB) ** 2 + (yA - yB) ** 2
BC2 = (xB - xC) ** 2 + (yB - yC) ** 2
CA2 = (xC - xA) ** 2 + (yC - yA) ** 2

if AB2 + BC2 == CA2 or BC2 + CA2 == AB2 or CA2 + AB2 == BC2:
    print("Yes")
else:
    print("No")