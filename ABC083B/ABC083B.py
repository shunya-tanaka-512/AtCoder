def get_sum_total(n, min_sum_digits, max_sum_digits):
    sum_total = 0  # 条件に当てはまる数の和
    for i in range(1, n + 1):
        sum_digits = sum(map(int, str(i)))  # 各桁の和1,2,3,4,5....7,8,9,10,2
        if min_sum_digits <= sum_digits <= max_sum_digits:
            sum_total += i
    return sum_total
