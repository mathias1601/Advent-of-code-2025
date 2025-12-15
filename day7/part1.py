class Splitter():
    def __init__(self):
        self.split = False

    def perform_split(self):
        self.split = True

    def is_split(self):
        return self.split

    def __str__(self):
        return "^"
    



grid = []

sum = 0

with open("input7.txt") as f:

    for line in f:
        line = line.strip("\n")
        
        # Change ^ into splitter objects
        line = [Splitter() if item == "^" else item for item in list(line)]

        grid.append(line)


y_axis = 0
x_axis = grid[0].index("S")

def recursive_split_count(x, y):

    global sum

    y += 1

    while y < len(grid):
        if str(grid[y][x]) == "^":
            
            if grid[y][x].is_split() == False:
                sum += 1
                grid[y][x].perform_split()

            recursive_split_count(x + 1, y)
            recursive_split_count(x - 1, y)
            return 
        y += 1


recursive_split_count(x_axis, y_axis)

print(sum)