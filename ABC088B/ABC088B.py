def get_score_diff(scores: list) -> int:
    # 奇数回は足す、偶数回は引く
    score_diff = 0
    new_scores = sorted(scores, reverse=True)  # sortedはlistを返す
    for i, score in enumerate(new_scores):  # enumerateで要素とインデックス番号取得
        if i % 2 == 0:
            score_diff += score
        else:
            score_diff -= score
    return score_diff
