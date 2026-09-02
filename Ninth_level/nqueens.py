def solveNQueens(board_size):
    results = []
    board = [["."] * board_size for _ in range(board_size)]

    def isSafe(board, row, col, board_size):
        # horizontal check — same row, scan across columns
        for check_col in range(board_size): #why for loop is -
            #suppose we are on row second we have to trace the whole col,
            #meaning for the above row the value can have Q
            if board[row][check_col] == "Q":
                return False

        # vertical check — same column, scan across rows
        for check_row in range(board_size):#same like horizontal
            if board[check_row][col] == "Q":
                return False

        #only upleft and upright are checked and while condition is till 0
        #because when we are moving up we can only go till 0
        #and why up, because we are already traversing to rows down, we
        #have filled the Q values in up rows only and not bottom

        # left diagonal (up-left) — row and col decrease together
        check_row, check_col = row, col
        while check_row >= 0 and check_col >= 0:
            if board[check_row][check_col] == "Q":
                return False
            check_row -= 1
            check_col -= 1

        # right diagonal (up-right) — row decreases, col increases
        check_row, check_col = row, col
        while check_row >= 0 and check_col < board_size:
            if board[check_row][check_col] == "Q":
                return False
            check_row -= 1
            check_col += 1

        return True #once all checks are passed return true

    def placeQueens(board, row, board_size, results):
        if row == board_size:#till the board size is not read we do not need to a
            #append the results do not worry
            results.append(["".join(r) for r in board])
            return

        for col in range(board_size): #for every column in first row
            if isSafe(board, row, col, board_size):
                # ires once a queen has been safely placed in every row on the current path 
                # (0 through board_size-1) - actual traversal
                board[row][col] = "Q"#mark the board box as q
                placeQueens(board, row + 1, board_size, results)#do the backtrack
                #if this call works fine, there would be issafe and next call
                #would be for next row, and backtrack would not be required
                #until the for loop has finished for the next row it is called for.
                #means in short explore the next branch fully, run all the for loop for col
                # for that row it is called for
                board[row][col] = "."   # backtrack

    placeQueens(board, 0, board_size, results) #start with 1st row
    return results