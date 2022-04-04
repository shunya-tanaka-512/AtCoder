def judge_str_match(character_str: str) -> str:
    character_str = character_str[::-1]
    word_list = ["dream"[::-1], "dreamer"[::-1], "erase"[::-1], "eraser"[::-1]]
    accu_str = ""  # これをfor文のなかで定義したらだめ
    judge = False
    for i in character_str:
        accu_str += i  # 後ろの文字から一文字ずつ蓄積
        if accu_str in word_list:  # リストにaccu_strと一致する要素あればTrue
            accu_str = ""  # 蓄積解除
            judge = True
        else:
            judge = False
    if judge:
        return "YES"
    else:
        return "NO"
