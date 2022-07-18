N, M, X, T, D = map(int, input().split())
# N歳の誕生日の時、身長Tcm
# 0~X歳までで身長がDcmずつ伸びる
# X歳の誕生日からN歳までは身長は変化してない
# MがX以下だったらT-(X*D)+ (M*D)が解
# それ以外ならTが解
if M <= X:
    ans = T - (X * D) + (M * D)
else:
    ans = T
print(ans)
