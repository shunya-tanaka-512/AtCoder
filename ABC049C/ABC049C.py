def judge_str_match(character_str: str) -> str:
    character_str = character_str[::-1]
    word_list = ["dream"[::-1], "dreamer"[::-1], "erase"[::-1], "eraser"[::-1]]
    while len(character_str) != 0:
        if character_str[:5] == word_list[0]:
            character_str = character_str[5:]
        elif character_str[:7] == word_list[1]:
            character_str = character_str[7:]
        elif character_str[:5] == word_list[2]:
            character_str = character_str[5:]
        elif character_str[:6] == word_list[3]:
            character_str = character_str[6:]
        else:
            return "NO"
            break
    return "YES"
