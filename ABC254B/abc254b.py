N = int(input())

A = []
inside_A = []
for i in range(N):
    for j in range(i + 1):
        if j == 0 or j == i:
            inside_A.append(1)
        else:
            inside_A.append(A[i - 1][j - 1] + A[i - 1][j])
    A.append(inside_A)
    inside_A = []

for k in range(N):
    print(*A[k])
