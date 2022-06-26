N, X = map(int, input().split())
# chr関数でN回分、65~90を回す
# 回数をカウントしてX番目で出力
count = 0
for i in range(65, 91):
    for j in range(N):
        count += 1
        if X == count:
            print(chr(i))
