def judge_possible_or_impossible(time_point_list: list) -> str:
    old_time = old_point_x = old_point_y = 0
    for time, point_x, point_y in time_point_list:
        move_possible_time = abs(old_time - time)  # 移動可能時間
        min_arrival_time = abs(old_point_x - point_x) + abs(old_point_y - point_y)  # 最短到着時間
        if (time + point_x + point_y) % 2 != 0 or move_possible_time < min_arrival_time:
            return "No"
        # 今回の入力値を記録
        old_time = time
        old_point_x = point_x
        old_point_y = point_y
    return "Yes"
