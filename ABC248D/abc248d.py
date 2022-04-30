n = int(input())
a = list(map(int, input().split()))
q = int(input())
queries = [(map(int, input().split())) for _ in range(q)]
for (l, r, x) in queries:
    if x in a[(l - 1):r]:
        print(a[(l - 1):r].count(x))
    else:
        print(0)
