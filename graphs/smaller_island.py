grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]


visited_land = []


def minimum_island(grid):
    min = 100
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            count = explore(grid, i, j)
            if count < min and count != 0:
                min = count

    return min


def explore(grid, row, col):
    if row < 0 or row >= len(grid):
        return 0
    if col < 0 or col >= len(grid[0]):
        return 0

    if grid[row][col] == 'W':
        return 0

    if [row, col] in visited_land:
        return 0
    visited_land.append([row, col])

    count = 1
    count += explore(grid, row-1, col)
    count += explore(grid, row+1, col)
    count += explore(grid, row, col-1)
    count += explore(grid, row, col+1)

    return count
