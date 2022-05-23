n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# aの中のmax値のインデックスを全て取得
a_max_index = [i for i, v in enumerate(a) if v == max(a)]
# 上のインデックスがb-1と被ってたらYes
new_b = [j-1 for j in b]
and_list = set(a_max_index) & set(new_b)
if len(and_list) != 0:
    print("Yes")
else:
    print("No")
