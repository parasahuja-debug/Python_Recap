def checkValidGrid(grid):
    n = len(grid)

    # move must start at (0,0)
    if grid[0][0] != 0:
        return False

    def is_valid(row, col, expected):
        # out of bounds, means we are moving out of grid and lets return false
        if row < 0 or col < 0 or row >= n or col >= n:
            return False
        # this cell's value doesn't match the move number we're looking for
        if grid[row][col] != expected: #the value we are looking for meaning
            # if i am on 1 i would be looking at 2, and if i am at 4 i would be looking
            # at 5 and so on. so if the value is not the interediate next, return false
            return False
        
        # reached the last move successfully
        if expected == n * n - 1: #this is the formula for calculating the last value
            # if i have a n*n grid then last value would be this only.
            return True

        # 8 possible knight moves
        # just remmber or mark a chess board, you will only get this 8 moves
        # from the position you are at. so hence, 8 moves.
        moves = [(-2, 1), (-1, 2), (1, 2), (2, 1),
                 (2, -1), (1, -2), (-1, -2), (-2, -1)]

        for dr, dc in moves:
            if is_valid(row + dr, col + dc, expected + 1):
                return True

        return False

    return is_valid(0, 0, 0)