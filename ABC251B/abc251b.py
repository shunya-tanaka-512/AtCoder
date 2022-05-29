import itertools

n, w = map(int, input().split())
# 重さが0のおもりが2個あるとする
weights = list(map(int, input().split())) + [0, 0]
nums = []  # 良い整数のリスト
num_combinations = list(itertools.combinations(weights, 3))
# num_combinationsの中で組み合わせ同士の和を調べる
num_combinations_sums = list(map(sum, num_combinations))
for j in num_combinations_sums:
    if j <= w:
        nums.append(j)
# 被っているリストを排除
nums = set(nums)
print(len(nums))
