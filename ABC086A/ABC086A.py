int_val_list = list(map(int, input().split()))  # 正の整数
int_val_first = int_val_list[0]
int_val_second = int_val_list[1]
if int_val_first % 2 != 0 and int_val_second % 2 != 0:
    print("Odd")
else:
    print("Even")
