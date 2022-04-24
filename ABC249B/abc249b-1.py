s = input()
if s.islower() or s.isupper():
    print("No")
    exit()
else:
    for i in range(len(s)):
        if s.count(s[i]) != 1:
            print("No")
            exit()
    print("Yes")
