def get_times_dividable_in_2(int_val_tuple):
    bin_val_tuple = [format(int_val, "b") for int_val in int_val_tuple]  # 2進数変換
    # 文字列の長さ-1が最後に見つかるインデックス番号-1
    zero_num = [len(bin_val) - bin_val.rfind("1") - 1 for bin_val in bin_val_tuple]
    return min(zero_num)
