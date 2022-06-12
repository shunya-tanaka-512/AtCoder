import math


N, K = map(int, input().split())
A = list(map(int, input().split()))
points_list = [list(map(int, input().split())) for _ in range(N)]


# 2点間の距離を求める関数
def calc_norm(a: list, b: list) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


# ライトなし座標とライトあり座標を分ける
points_N_list = []
points_K_list = []
for i in range(1, N+1):
    if i in A:
        points_K_list.append(points_list[i-1])
    else:
        points_N_list.append(points_list[i-1])

# ライトなし座標とライトあり座標の最短距離のリストの中の最大値を求める
min_norms = []
for points_N in points_N_list:
    tmp_norms = []  # １つのライトなし座標からの距離が一旦入る
    for points_K in points_K_list:
        tmp_norms.append(calc_norm(points_N, points_K))
    min_norms.append(min(tmp_norms))
print(max(min_norms))
