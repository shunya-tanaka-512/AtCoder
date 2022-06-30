N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))
# N個のマス、K個のコマ、最初左からi番目のコマはマスAにある
# Aはコマの位置 [1, 3, 4]
# Lは操作するコマの位置  [3, 3, 1, 1, 2]
# Aのインデックス(i-1)番目（＝左からL番目のコマ） の値がNと等しいとき一番右なので次へ
# そうでない時もしA[i-1]+1の値がAにあれば次へ
# それ以外はA[i-1]値を+1する
# 最終的にAの値を出力する

for i in L:
    if A[i-1] == N:
        continue
    elif (A[i-1]+1) in A:
        continue
    else:
        A[i-1] = A[i-1]+1
print(*A)
