lst = list(map(int, input().split()))
a = lst[0]
b = lst[1]
k = lst[2]
print(lst)
cnt = 0
# AにKをかけてその値に再度Kをかけ続けてBになったら終わり
while a < b:
    a = a * k  # a = 1 * 2
    cnt += 1
print(cnt)
