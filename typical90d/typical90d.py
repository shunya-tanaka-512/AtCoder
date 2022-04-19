def get_cell_totals(h: int, w: int, cell_nums: list) -> list:
    row_totals = list(map(sum, cell_nums))  # 各行の合計 [9, 22, 21, 28]
    column_totals = list(map(sum, zip(*cell_nums)))  # 各列の合計 [22, 20, 20, 18]
    cell_totals = []
    for i in range(h):
        cell_total = []
        for j in range(w):
            cell_total.append(row_totals[i] + column_totals[j] - cell_nums[i][j])
        cell_totals.append(cell_total)
    return cell_totals
