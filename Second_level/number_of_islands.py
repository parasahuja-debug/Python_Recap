
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands=0 #initialise
        #rows
        i=len(grid)
        #columns
        j=len(grid[0])

        def island(r,c):
            if r<0 or c<0 or r>=i or c>=j or grid[r][c]=="0":
                return
            #i have gone out of grid - r<0 or c<0 or r>=i or c>=j
            grid[r][c]="0" #we are making island to 0 so that it cannot be traced
            #again
            island(r-1,c) #top - r ir row , move back row and same column
            island(r+1,c) #bottom - r is row. move extra row and same column
            island(r,c-1) #left - c is column , same row and column back
            island(r,c+1) #right - c is column, same row and column ahead

        for r in range(i):
            for c in range(j):
                if grid[r][c]=="1": #only where island exists
                    islands+=1 #found the island so put that to 1
                    island(r,c) #now find the neighbour if any
        return islands

#solution would work in leet code.
# if we have vertical and horizontal both and both direction,
# 1 from 1 then that is one island all are parts.

#if horizontal and vertical 1s are not there, then that 1 is the only area for island

#if only horizontally i can find one not vertical , then that is also part of same 
# island that we are traversing 

#if only vertical, i can find only vertical to 1, then that is part of same island
#that we are traversing now