input_list = []
for i in input():
    input_list.append(int(i))  # [1, 1, 0]
count = 0
for input in input_list:
    if input == 1:
        count += 1
print(count)
