a, b, k = (map(int, input().split()))
cnt = 0
# AにKをかけてその値に再度Kをかけ続けてBになったら終わり
while a < b:
    a = a * k  # a = 1 * 2
    cnt += 1
print(cnt)
