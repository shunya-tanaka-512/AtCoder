import collections


n, k = map(int, input().split())
strings = [input() for _ in range(n)]
num_of_char_types = []
# ビット全探索
for i in range(1 << n):
    selected_strings = []
    for j in range(n):
        if i >> j & 1:
            selected_strings.append(strings[j])
    combined_strings = "".join(selected_strings)  # selected_stringsの文字列結合
    char_counter = collections.Counter(combined_strings)  # 要素の出現回数を調べる
    # valueがkのkeyを探す
    keys = [key for key, value in char_counter.items() if value == k]
    num_of_char_types.append(len(keys))  # keysの要素数（文字の種類数）をリスト化
print(max(num_of_char_types))
