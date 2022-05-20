# opn the file by specifying full path
with open("/home/andy/ws/ctpsws/lessons/src/lessons/dunham/grid.csv") as f:
    # read each line removing newlines and making it a list
    # needs to be a list because it must be immutable
    grid = [line.strip().split(",") for line in f]

# grid is now a map of the contents of the file
print(grid)

# access or update individual cell
grid[2][3] = "X"
for line in range(len(grid)):
    for column in range(len(grid[0])):
        print(grid[line][column])
