
# Given a chessboard of size N x N and a knight placed on cell (0, 0), 
# find a sequence of moves such that the knight visits every cell on the
# board exactly once. Print the board showing the order in which cells were visited 
# (cell values from 0 to N²-1), or report that no such tour exists.

def knight_tour(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2] #rows of 8 moves
    move_y = [1, 2, 2, 1, -1, -2, -2, -1] #columns of 8 moves

    def solve(row, col, count):
        # out of bounds
        if row < 0 or col < 0 or row >= N or col >= N: #out of bound
            return False

        # already visited
        if board[row][col] == 1: #already visited
            return False

        # place
        board[row][col] = 1 #place at valid location

        # base case: all N*N cells touched
        if count == N * N - 1: #if the count is found return true
            return True

        # try all 8 moves
        for i in range(8):
            if solve(row + move_x[i], col + move_y[i], count + 1):
                return True

        # backtrack — unplace, since this path failed
        board[row][col] = 0 #backtrack if the position from where 8 moves are called
        #is wrong, as knight can select any one of the 8 moves and set it
        #as 1 and move ahead from there and call 8 moves
        #if all the 8 moves are not right then it has to backtrack, 
        #and eventually the main 8 moves would be checked, even if 
        #one has responded true, it has already been marked as trye at 31 line
        #but eventually the function would end when 22 line is met
        return False

    if solve(0, 0, 0): #call for 0,0
        for row in board:
            print(row)
    else:
        print(f"No knight's tour exists for N = {N}")


knight_tour(5) #starts from here