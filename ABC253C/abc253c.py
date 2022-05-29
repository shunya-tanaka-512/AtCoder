q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]
s = []
for i in range(q):
    if queries[i][0] == 1:
        s.append(queries[i][1])
    if queries[i][0] == 2:
        remove_count = min(queries[i][2], s.count(queries[i][1]))
        for j in range(remove_count):
            s.remove(queries[i][1])
    if queries[i][0] == 3:
        print(max(s) - min(s))
