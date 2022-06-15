N, A, B = map(int, input().split())
# "."のみで箱を先に用意する
field = [["."] * B * N for _ in range(A * N)]

# # マス（i,j）が属するタイルをi//A,j//Bで求める
for i in range(A * N):
    for j in range(B * N):
        # i//A+j//Bが偶数の時白、奇数の時黒
        if (i//A + j//B) % 2 == 1:
            field[i][j] = "#"

for k in field:
    print("".join(k))
