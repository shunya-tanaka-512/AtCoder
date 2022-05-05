n = int(input())
a = list(map(int, input().split()))
q = int(input())
queries = [(map(int, input().split())) for _ in range(q)]
for (l, r, x) in queries:
    print(a[(l - 1):r].count(x))
