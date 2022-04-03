def judge_str_match(character_str: str) -> str:
    # この順でreplaceしないと文字が被っているところが先にreplaceされてしまう
    replaced_str = character_str.replace('eraser', '').replace('erase', '').replace('dreamer', '').replace('dream', '')
    if len(replaced_str) == 0:
        return "YES"
    else:
        return "NO"
