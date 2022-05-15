import itertools

n, w = map(int, input().split())
weights = list(map(int, input().split()))
nums = []  # 良い整数のリスト
for i in range(1, 4):
    num_combinations = list(itertools.combinations(weights, i))
    # num_combinationsの中で組み合わせ同士の和を調べる
    num_combinations_sums = list(map(sum, num_combinations))
    for j in num_combinations_sums:
        if j <= w:
            nums.append(j)
# 被っているリストを排除
nums = set(nums)
print(len(nums))
