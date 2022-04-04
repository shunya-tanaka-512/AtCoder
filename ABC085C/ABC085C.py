def get_bill_combination(num_of_bills: int, sum_total: int) -> list:
    TEN_THOUSAND = 10000
    FIVE_THOUSAND = 5000
    THOUSAND = 1000
    # 初期値をsum_total円があり得ない場合の-1 -1 -1とする
    yen10000_num, yen5000_num, yen1000_num = [-1, -1, -1]
    for i in range(num_of_bills + 1):
        for j in range(num_of_bills - i + 1):  # 一万円の枚数引いた回数
            if (
                TEN_THOUSAND * i
                + FIVE_THOUSAND * j
                + THOUSAND * (num_of_bills - i - j)  # 一万円と五千円引いた枚数=千円の枚数
                == sum_total
            ):
                yen10000_num, yen5000_num, yen1000_num = [i, j, num_of_bills - i - j]
    return [yen10000_num, yen5000_num, yen1000_num]
