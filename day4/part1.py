main_grid = []
total_rolls = 0 

# Helper method for checking whether a combination of row or column is valid
def is_spot_valid(row, column):
        if row > len(main_grid[0]) -1 or column > len(main_grid) -1 or row < 0 or column < 0:
            return None
       
        return main_grid[column][row]

# Helper method for couting the amount of adjecent roll in a spot in the main_grid
def count_adjecent_rolls(row, column):
    count = 0

    for y in range(-1, 2):
        for x in range(-1, 2):
            if is_spot_valid(row + x, column + y) == "@" and (x, y) != (0, 0):
                count += 1
   
    return count


with open("input4.txt") as f:

    for line in f:
        row = list(line.strip("\n"))
        main_grid.append(row)

    for y in range(len(main_grid)):
        for x in range(len(row)):
            if main_grid[y][x] == "@" and count_adjecent_rolls(x, y) < 4:
                total_rolls += 1

print(total_rolls)


