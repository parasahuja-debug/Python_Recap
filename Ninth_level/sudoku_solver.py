def solveSudoku(board):
    def is_safe(row, col, digit):
        # horizontal check
        for j in range(9): #we are traversing through the entire row
            #and finding the digit so, column which is j here , is moved
            if board[row][j] == digit:
                return False
        # vertical check
        for i in range(9): #we are traversing through the entire column
            #and finding the digit , so row which is i here, is moved
            if board[i][col] == digit:
                return False
        # 3x3 grid check
        start_row = (row // 3) * 3 #finding through the entire grid row
        start_col = (col // 3) * 3 #grid column 3 is used as we have kept the
# row	- row // 3  -	(row // 3) * 3 = start_row
# 0 -	0 -	0
# 1	0	0
# 2	0	0
# 3	1	3
# 4	1	3
# 5	1	3
# 6	2	6
# 7	2	6
# 8	2	6
        #internal grid as 3*3
        for i in range(start_row, start_row + 3):#+3 is 3 blocks i have to traverse
            for j in range(start_col, start_col + 3):
                if board[i][j] == digit:
                    return False
        return True

    def helper(row, col):
        if row == 9:  # base case: walked off last row -> solved
            return True

        next_row, next_col = row, col + 1 #this is done to examine the next calls
        if next_col == 9:#we are traversing each row so, we might hit the dead end
            #of columns so if the next column is outside the grid
            #move to next row
            next_row, next_col = row + 1, 0

        if board[row][col] != '.':  # already filled -> move on
            return helper(next_row, next_col)#if for my sudokyu, the block i am at
        #does not need filling of digits 1 to 9 so move to next

        for digit in '123456789': #fill out the block with eiher digit
            if is_safe(row, col, digit):
                board[row][col] = digit #put the number on the block if it is safe to
                if helper(next_row, next_col):#this is there because we
                    #might hit the deadene and not have any right value in the row
                    return True
                board[row][col] = '.'  # backtrack

        return False  # nothing worked in this cell

    helper(0, 0)