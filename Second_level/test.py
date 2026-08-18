class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

# class Solution:
    # def maxDepth(self,root): Recursion
    #     if not root:
    #         return 0
    #     return 1 + max(Solution().maxDepth(root.left),Solution().maxDepth(root.right))
    # def maxDepth(self,root): #bfs queue and dfs stack
    #     if not root:
    #         return 0
    #     level=0
    #     queue=deque([root])
    #     while queue:
    #         print("enter queue")
    #         for i in range(len(queue)):
    #             print("enter if")
    #             node=queue.popleft() #remove from left and add from right
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #         level+=1
    #         print(level,queue)
    #     return level
    
# class Solution:
#     def maxDepth(self,root):
#         result=[]
#         queue=deque([root])
#         while queue:
#             array=[]
#             for i in range(len(queue)):
#                 node=queue.popleft()
#                 array.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             result.append(array)
#         return result

        
# queue has root, queue pop from left if queue has something
# append left and right, 9,20 level 1
# while queue - pop only 20 left, 20,null,null
# for loop only 20 pop, add 15,7 , null,null,15,7
#while queue - null pop, null,15,7, cant appendif 


# class Solution:
#     def lowestCommonAncestor(self, root, p, q):
#         if not root:
#             return None
#         if p==root or q==root:
#             return root
#         left=Solution().lowestCommonAncestor(root.left,p,q)
#         right=Solution().lowestCommonAncestor(root.right,p,q)
#         if left and right:
#             return root
#         elif left:
#             return left
#         else:
#             return right

#for me lowest common is 9, 27
# if no root, then nothing is lowest common
# if p is root and q is root , then root is the lowest common ancestor
# now search for left subtree of root, root.left is root and p and p are to be searched again
# root.left is 9 and p is 9 what we were finding is 9
# left is found
#20 -, p, q , now q would be equated
# q==root no, q is 27, left of 20, 27, 27 found, no right
        
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         island=0
#         rows=len(grid)
#         column=len(grid[0])
#         def rightlefttopbot(r,c):
#             if r<0 or c<0 or r >= rows or c >= column or grid[r][c]=="0":
#                 return None
#             grid[r][c]="0"
#             rightlefttopbot(r-1,c)
#             rightlefttopbot(r+1,c)
#             rightlefttopbot(r,c-1)
#             rightlefttopbot(r,c+1)
#         for r in range(rows):
#             for c in range(column):
#                 if grid[r][c]=="1":
#                     island+=1
#                     rightlefttopbot(r,c)
#         return island

class Solution:
    def isValidBST(self, root) -> bool:
        def valid(node, right, left):
            if not node:#no node, return true, when recursion, it might be checki
                #ing the nodes where leaf nodes are not there
                #and eventually combined ans is returned.
                #except for the main root where if that is even not there it is valid
                return True
            if not ((node.val<right) and (node.val>left)):#oopposit of what we want
                #demorgan's law, not a and b is also not a or not b.
                #so can be written that way
                return False
            return (valid(node.left,node.val,left) and valid(node.right,right,node.val))
            #check for both left and right node
        return valid(root,float("inf"),float("-inf"))#main condition root should be in -inf to +inf 



root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(20)

root.right.left = TreeNode(35)
root.right.right = TreeNode(27)
print(Solution().isValidBST(root))

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)

# root.right.left = TreeNode(27)
# root.right.right = TreeNode(35)
# print(Solution().lowestCommonAncestor(root,9,15))