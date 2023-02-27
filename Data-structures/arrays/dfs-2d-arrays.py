matrix = [
    [1, 2, 3, 4, 5], 
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs2DTraversal(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    # seen = [[False] * COLS  for _ in range(ROWS)]
    visited = set()
    values = []

    def dfs(matrix, row, col,):

        if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in visited:
            return 

        values.append(matrix[row][col])
        visited.add((row, col))
                # Up, Right, Down, Left
        for r, c in directions:
        
            dfs(matrix, row + r, col + c)


    dfs(matrix, 0, 0)

    return values


print(dfs2DTraversal(matrix))



