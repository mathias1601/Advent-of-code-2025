points = []
largest_area = 0

with open ("input9.txt") as f:
    for line in f:
        line = line.strip("\n")
        line = line.split(",")
        line = [int(value) for value in line]
        points.append(line)

for point1 in points:
    for point2 in points:
        if point1 == point2:
            pass
        area = (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)

        if area > largest_area:
            largest_area = area

print(largest_area)