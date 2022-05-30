h, w = map(int, input().split())
strings = [input() for _ in range(h)]

# コマのあるマスの座標求める
first_o_is_found = False
second_o_is_found = False
for i in range(h):
    for j in range(w):
        if not first_o_is_found:
            if strings[i][j] == "o":
                first_o_h, first_o_w = i, j
                first_o_is_found = True
        elif strings[i][j] == "o":
            second_o_h, second_o_w = i, j
            second_o_is_found = True
            break
    if second_o_is_found:
        break
# 座標の差分で移動回数を求める
transit_times = abs(first_o_h - second_o_h) + abs(first_o_w - second_o_w)
print(transit_times)
