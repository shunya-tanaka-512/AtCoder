def get_pattern_select_coins(yen500_num, yen100_num, yen50_num, yen_sum):

    FIVE_HUNDRED = 500
    ONE_HUNDRED = 100
    FIFTY = 50

    count = 0
    # 答えゼロパターン：合計金額に持っている硬貨が足りない時
    if (
        yen500_num * FIVE_HUNDRED + yen100_num * ONE_HUNDRED + yen50_num * FIFTY
        < yen_sum
    ):
        return 0
    # 答えゼロパターン：合計金額が150円とかなのに50円持ってない時
    elif yen_sum / 50 % 2 != 0 and yen50_num == 0:
        return 0
    else:
        for i in range(yen500_num + 1):
            if FIVE_HUNDRED * i > yen_sum:
                break
            remain500 = yen_sum - FIVE_HUNDRED * i
            for j in range(yen100_num + 1):
                if ONE_HUNDRED * j > remain500:
                    break
                # 500円と100円を引いた残額が50円で払えて、50の倍数の時カウントアップ
                remain100 = remain500 - ONE_HUNDRED * j
                if remain100 <= 50 * yen50_num:
                    if remain100 % 50 == 0:
                        count += 1
        return count
