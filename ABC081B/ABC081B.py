int_val_num = int(input())  # 整数の個数
int_val_list = list(map(int, input().split()))  # 正の整数
bin_val_list = [format(int_val, "b") for int_val in int_val_list]  # 2進数変換
# 文字列反転['0001', '0011', '000101']
return_bin_val_list = [bin_val[::-1] for bin_val in bin_val_list]
# 文字列の位置取得[3, 2, 3]
find_1 = [return_bin_val.find("1") for return_bin_val in return_bin_val_list]
print(min(find_1))
