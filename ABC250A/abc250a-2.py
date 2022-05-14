h, w = map(int, input().split())
r, c = map(int, input().split())
adjacent_squares = 0
# 上にマスがある r≠1
if r != 1:
    adjacent_squares += 1
# 下にマスがある r≠h
if r != h:
    adjacent_squares += 1
# 左にマスがある c≠1
if c != 1:
    adjacent_squares += 1
# 右にマスがある c≠w
if c != w:
    adjacent_squares += 1
print(adjacent_squares)
