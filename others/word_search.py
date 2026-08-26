#grid given we have to find a word - it has to be made from adjacent characters only
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
# word = "ABCCED"

# O(m × n × 3^L)
#3 direction for each word and 
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board) #row
        n = len(board[0]) #column

        def dfs(row, col, index):
            # We found the complete word
            if index == len(word): #if through the iterative call we finally found the index = length of word
                return True

            # Out of bounds
            if row < 0 or row >= m or col < 0 or col >= n:
                return False #if i am ouside the grid

            # Character doesn't match
            if board[row][col] != word[index]:#if the word doesnt match
                # and most important as we are marking the word as # the loop breaks
                return False

            # Mark current cell as visited
            temp = board[row][col] #this is for later if we have to trace the
            #grid again
            board[row][col] = "#"

            # Try top, bottom, left, right
            found = ( #either it will give the entire word or false
                dfs(row - 1, col, index + 1) or
                dfs(row + 1, col, index + 1) or
                dfs(row, col - 1, index + 1) or
                dfs(row, col + 1, index + 1)
            )

            # Backtrack: restore the cell
            board[row][col] = temp#because we have looked out for all the options in 
            #all the direction lets mark it as back to the value

            return found #either true or false, and we will lool for the next first character in the grid and start the loop

        # Find the first character
        for i in range(m): #row
            for j in range(n): #column
                if board[i][j] == word[0]: #If we find the first character our
                #journey starts
                    if dfs(i, j, 0): #call the function
                        return True

        return False