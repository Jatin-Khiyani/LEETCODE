grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

m, n = len(grid), len(grid[0])


def find_ones(i, j):

    if i in range(m) and j in range(n):
        grid[i][j] = "0"
        if (i in range(m) and j + 1 in range(n)) and grid[i][j + 1] == "1":
            find_ones(i, j + 1)
        if (i in range(m) and j - 1 in range(n)) and grid[i][j - 1] == "1":
            find_ones(i, j - 1)
        if (i + 1 in range(m) and j in range(n)) and grid[i + 1][j] == "1":
            find_ones(i + 1, j)
        if (i - 1 in range(m) and j in range(n)) and grid[i - 1][j] == "1":
            find_ones(i - 1, j)

    return grid


island = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == "1":
            island += 1
            grid = find_ones(i, j)

print(island)
