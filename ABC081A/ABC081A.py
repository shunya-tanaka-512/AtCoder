def get_number_of_marbles(input_num):
    input_list = [int(i) for i in str(input_num)]  # 文字列を一文字ずつ取り出してint()処理
    count = 0
    for input in input_list:
        if input == 1:
            count += 1
    return count
