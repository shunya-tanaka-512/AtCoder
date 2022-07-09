import math


N, X = map(int, input().split())
num = math.ceil(X / N) - 1
print(chr(ord("A") + num))
