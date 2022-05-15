s = input()
for i in range(1, 7):
    new_s = s * i
    if len(new_s) == 6:
        print(new_s)
        break
