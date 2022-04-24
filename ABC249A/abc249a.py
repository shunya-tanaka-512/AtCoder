a, b, c, d, e, f, x = map(int, input().split())
# a + cで割った余りがaより小さい時
if a > (x % (a + c)):
    takahashi_time = (x // (a + c)) * a + x % (a + c)
# a + cで割った余りがa以上->あと１回a秒歩く+休み(ノーカウント)
else:
    takahashi_time = (x // (a + c)) * a + a
takahashi_dist = takahashi_time * b

if d > (x % (d + f)):
    aoki_time = (x // (d + f)) * d + x % (d + f)
else:
    aoki_time = (x // (d + f)) * d + d
aoki_dist = aoki_time * e

if takahashi_dist > aoki_dist:
    print("Takahashi")
elif takahashi_dist < aoki_dist:
    print("Aoki")
else:
    print("Draw")
