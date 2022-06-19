N = int(input())
names = [list(input().split()) for _ in range(N)]
# まず姓で調べて他の人と一致したかどうかを記録しておく
# 次に名で調べて、姓名どちらも他の人と一致していたらNoを出力して終了
# どちらか一致しなかったら次へ
# 最後までNoにならずに処理が終了したらYes
for i in range(N):
    is_s_matched = False
    for nickname in names[i]:
        for j in range(N):
            if i != j:
                # is_s_matchedがTrue時に名前も一致していたらNo出力して終了
                if is_s_matched:
                    if nickname in names[j]:
                        print("No")
                        exit()
                # 他の人と名字が一致している
                elif nickname in names[j]:
                    is_s_matched = True
print("Yes")
