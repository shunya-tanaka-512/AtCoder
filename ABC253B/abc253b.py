h, w = map(int, input().split())
strings = [input() for _ in range(h)]
# コマのあるマスの座標求める
addresses = []
for i in range(h):
    if "o" in strings[i]:
        address = []
        o_index = strings[i].find("o")
        address.append(i)
        address.append(o_index)
        addresses.append(address)
# 座標の差分で移動回数を求める
transit_times = abs(addresses[0][0] - addresses[1][0]) + abs(addresses[0][1] - addresses[1][1])
print(transit_times)
