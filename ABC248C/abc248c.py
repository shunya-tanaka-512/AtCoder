import itertools

lst = list(map(int, input().split()))
n = lst[0]  # 31
m = lst[1]  # 41
k = lst[2]  # 592
cnt = 0
# n項の数列で、要素は１以上m以下、要素の和がk以下
m_list = list(range(1, (m + 1)))
# m_listからn個の数を順列・重複ありで選ぶ
for i in itertools.product(m_list, repeat=n):
    if sum(i) <= k:
        cnt += 1
cnt %= 998244353
print(cnt)
