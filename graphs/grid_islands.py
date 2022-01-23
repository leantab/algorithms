grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]

visited_land = []


def island_count(grid):
    count = 0

    for i in grid:
        for j in grid[0]:
            if j not in visited_land:
                if explore(grid, i, j):
                    count += 1

    return count


def explore(grid, row, col):
    if row < 0 or row >= len(grid):
        return False
    if col < 0 or col >= len(grid[0]):
        return False

    if grid[row][col] == 'W':
        return False

    if [row, col] in visited_land:
        return False
    visited_land.append([row, col])

    explore(grid, row-1, col)
    explore(grid, row+1, col)
    explore(grid, row, col-1)
    explore(grid, row, col+1)

    return True
