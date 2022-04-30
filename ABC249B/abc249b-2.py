s = input()
accumulated_s = ""
is_lower = False
is_upper = False
is_mixed_case = False
for i in range(len(s)):
    accumulated_s = accumulated_s + (s[i])
    # 既出の文字が出た時点でNoをprintしてexit
    if len(accumulated_s) != len(set(accumulated_s)):
        print("No")
        exit()
    if not is_mixed_case:
        if s[i].islower():
            is_lower = True
        elif s[i].isupper():
            is_upper = True
        if is_lower and is_upper:
            is_mixed_case = True
# is_mixed_caseフラグがFalseのままならNoをprintしてexit
if not is_mixed_case:
    print("No")
else:
    print("Yes")
