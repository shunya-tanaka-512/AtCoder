N = int(input())
A = list(map(int, input().split()))
P = 0
# コマがどのマスにいるか管理するリスト用意
# Aのリストから一つずつ順に値を取り出す
# 取り出した値を、その値のインデックス以下のコマ全部にたす
# 上の処理が終わった時点でコマの値が４以上である個数が求めたいPの値になる
batters = [0] * N
for i in range(N):
    for j in range(i+1):
        batters[j] = batters[j] + A[i]
P = len([k for k in batters if k >= 4])
print(P)
