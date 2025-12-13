import numpy as np

all_lists = []
sum = 0

with open("input6.txt") as f:

    for line in f:

        line = line.strip("\n")
        line = line.split(" ")

        # To remove all occurenzes of empty spaces
        line = [item for item in line if item != ""]

        all_lists.append(line)

all_lists = np.array(all_lists).T


for list in all_lists:

    sum_to_add = int(list[0])

    for i in range(1, len(list) - 1):
        if list[len(list) - 1] == "*":
            sum_to_add *= int(list[i])
        else:
            sum_to_add += int(list[i])
    
    sum += sum_to_add

print(sum)