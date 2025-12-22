import sys

sys.setrecursionlimit(2000)


light_diagrams = {}

with open("input10.txt") as f:

    for line in f:
        line = line.strip("\n")
        line = line.translate(str.maketrans("", "", "[](),"))
        line = line.split(" ")
        
        tuples = []

        for i in range(1, len(line) - 1):
            tuples.append(line[i])

        light_diagrams[line[0]] = tuples

def recursive_search(goal_node, current_node, distance, shortest_distance_dict):
    
    if current_node not in shortest_distance_dict:
        shortest_distance_dict[current_node] = distance
    else:
        if distance < shortest_distance_dict[current_node]:
            shortest_distance_dict[current_node] = distance
        else:
            return

    if current_node == goal_node:
        return

    distance += 1

    for button in light_diagrams[goal_node]:

        new_node = current_node

        for num in button:

            index = int(num)
         
            if new_node[index] == '.':
                new_node = new_node[:index] + "#" + new_node[index + 1:]
            else:
                new_node = new_node[:index] + "." + new_node[index + 1:]

        recursive_search(goal_node, new_node, distance, shortest_distance_dict)


sum = 0


for goal in light_diagrams:
    distance_dict = {}
    starting_point = "." * len(goal)
    recursive_search(goal, starting_point, 0, distance_dict)
    sum += distance_dict[goal]

print(sum)


