h, w = map(int, input().split())
r, c = map(int, input().split())
adjacent_squares = 0
if (h, w) == (1, 1):
    adjacent_squares = 0
    print(adjacent_squares)
    exit()
if h != 1 and w != 1:
    if (r, c) == (1, 1) or (r, c) == (1, w) or (r, c) == (h, 1) or (r, c) == (h, w):
        adjacent_squares = 2
    elif r != 1 and r != h and c != 1 and c != w:
        adjacent_squares = 4
    else:
        adjacent_squares = 3
if h == 1:
    if c == 1 or c == w:
        adjacent_squares = 1
    else:
        adjacent_squares = 2
if w == 1:
    if r == 1 or r == h:
        adjacent_squares = 1
    else:
        adjacent_squares = 2
print(adjacent_squares)
