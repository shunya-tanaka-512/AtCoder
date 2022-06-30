N = int(input())
names = [list(input().split()) for _ in range(N)]

for i in range(N):
    is_s_matched = False
    for nickname in names[i]:
        for j in range(N):
            if i != j:
                # names[i]の姓も名も自分以外の人の姓および名と一致していたらNo出力して終了
                if is_s_matched:
                    if nickname in names[j]:
                        print("No")
                        exit()
                # names[i]の姓が自分以外の人の姓および名と一致しているときis_s_matchedがTrueにする
                elif nickname in names[j]:
                    is_s_matched = True
                    break  # 姓はもう調べなくていいので名を調べる
        if not is_s_matched:
            break  # names[i]の姓が自分以外の人の姓および名のどちらとも一致しないので次のnamesへ
print("Yes")
