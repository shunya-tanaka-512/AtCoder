def get_sum_total(int_num, digit_sum_a, digit_sum_b):
    sum_total = 0  # 条件に当てはまる数の和
    for i in range(1, int_num + 1):
        digit_sum = sum([int(j) for j in str(i)])  # 各桁の和1,2,3,4,5....7,8,9,10,2
        if digit_sum_a <= digit_sum <= digit_sum_b:
            sum_total += i
    return sum_total
