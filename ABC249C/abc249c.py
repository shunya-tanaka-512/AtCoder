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
    # keyの要素数を調べる=keyの要素数分の1を足す
    key_count = sum(1 for _ in filter(lambda items: items[1] == k, char_counter.items()))
    num_of_char_types.append(key_count)  # keyの要素数（文字の種類数）をリスト化
print(max(num_of_char_types))
