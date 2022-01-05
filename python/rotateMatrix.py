def rotate_matrix(grid):
    """given an NxN matrix, rotate by 90 degrees
    :type grid: List[List[int]]
    :rtype List[List[int]]
    """
    n = len(grid)
    rotated = []
    for i in range(n):
        rotated.append([])
    for i in range(n):
        for k in range(n):
            rotated[n-1-k].append(grid[i][k])

    return rotated


in_grid = [
    [1, 2, 1, 2],
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [1, 2, 3, 4]
]
out = rotate_matrix(in_grid)
for row in out:
    print(row)
