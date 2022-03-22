intl_val_num = int(input())  # 整数の個数
int_val_list = list(map(int, input().split()))  # 正の整数
count = 0
isOdd = False
while True:
    for int_val in int_val_list:
        # 奇数だったら次の処理へ
        if int_val % 2 != 0:
            isOdd = True
            break
    # 奇数だったらwhileを抜ける
    if isOdd:
        break
    # 2で割ってリストへ代入
    int_val_list = [int_val / 2 for int_val in int_val_list]
    count += 1

print(count)
