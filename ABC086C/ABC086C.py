def judge_possible_or_impossible(time_point_list: list) -> str:
    for time_point in time_point_list:
        time, point_x, point_y = time_point
        if time >= (point_x + point_y) and time % 2 == (point_x + point_y) % 2:
            return "Yes"
        else:
            return "No"
