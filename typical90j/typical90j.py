def get_score_totals(n: int, classes_and_scores: list, q: int, id_nums: list) -> list:
    l_id_nums = [a[0] - 1 for a in id_nums]
    r_id_nums = [b[1] for b in id_nums]
    classes = [c[0] for c in classes_and_scores]
    scores = [d[1] for d in classes_and_scores]
    score_totals = []

    score_accms = [[0, 0]]  # 0のインデックス追加
    score_accm_1 = 0
    score_accm_2 = 0
    for i in range(n):
        if classes[i] == 1:
            score_accm_1 += scores[i]
        else:
            score_accm_2 += scores[i]
        score_accms.append([score_accm_1, score_accm_2])

    for j in range(q):
        score_total_1 = score_accms[r_id_nums[j]][0] - score_accms[l_id_nums[j]][0]
        score_total_2 = score_accms[r_id_nums[j]][1] - score_accms[l_id_nums[j]][1]
        score_totals.append([score_total_1, score_total_2])
    return score_totals
