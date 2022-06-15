import math


N = int(input())


def print_row(row_num: int) -> list:
    row = []
    for r in range(row_num+1):
        comb_num = math.comb(row_num, r)
        row.append(comb_num)
    return print(*row)


for i in range(N):
    print_row(i)
