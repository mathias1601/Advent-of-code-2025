list_of_ranges = []
list_of_ingredients = []
sum = 0

with open("input5.txt") as f:

    new_line_passed = False

    for line in f:
        line = line.strip("\n")

        if line == "":
            new_line_passed = True
        elif new_line_passed:
            list_of_ingredients.append(int(line))
        else:
            list_of_ranges.append(line)


for ingredient in list_of_ingredients:
    for num_range in list_of_ranges:
        
        num_range = num_range.split("-")

        if ingredient >= int(num_range[0]) and ingredient <= int(num_range[1]):
            sum += 1
            break

print(sum)
        