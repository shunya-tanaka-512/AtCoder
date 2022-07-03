K = int(input())
if K >= 60:
    MM = 21 + (K // 60)
    HH = str(K % 60).zfill(2)
else:
    MM = 21
    HH = str(K).zfill(2)
print(f"{MM}:{HH}")
