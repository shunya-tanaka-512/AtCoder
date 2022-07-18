import collections


S = input()
if len(set(S)) == 3:
    print(S[0])
elif len(set(S)) == 2:
    # 重複してない文字を探す
    ans = [k for k, v in collections.Counter(S).items() if v == 1]
    print(ans[0])
else:
    print(-1)
