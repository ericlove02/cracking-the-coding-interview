def zero_matrix(grid):
    """if an element of an MxN matrix is 0, its entire row and column set to 0
    :type grid: List[List[int]]
    :rtype List[List[int]]
    """
    copy = grid
    m = len(grid)
    n = len(grid[0])
    rows = []
    cols = []

    # find the zeros in the matrix and change row and col in copy to 0s
    for i in range(m):
        for k in range(n):
            if grid[i][k] == 0:
                # i: row to remove, k: col to remove
                rows.append(i)
                cols.append(k)
    rows = sorted(set(rows))
    cols = sorted(set(cols))
    for row in rows:
        for col in range(n):
            copy[row][col] = 0
    for col in cols:
        for row in range(m):
            copy[row][col] = 0

    return copy


in_grid = [
    [1, 2, 1, 2, 1],
    [1, 3, 0, 7, 9],
    [2, 4, 6, 8, 10],
    [0, 2, 3, 4, 0]
]

for row in in_grid:
    print(row)
out = zero_matrix(in_grid)
print()
for row in out:
    print(row)
