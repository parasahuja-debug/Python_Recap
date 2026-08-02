# So what are we doing heer
# we have been giving a binary tree and we are to calculate the max depth from the root node to either side
# it can be towards left or towards right
#first codition is obvious if rrot is empty length is 0
# and to solve the problem we have three solutions.
#recursion, second is BFS, last is iterative DFS.

    #     3
    #   /   \
    #  9     20
    #       /  \
    #      15   7

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     return 1 + max(Solution().maxDepth(root.left),Solution().maxDepth(root.right)) #1 because root is there, amd iteratively callingleft and right
    #     #nodes
    
    # #BFS- queue usage
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     level=0 #count the levels and you are done
    #     queue=deque([root]) #you need to pop and put in queue and increase the length
    #     while queue:
    #         for i in range(len(queue)):
    #             node=queue.popleft() #pop the element
    #             if node.left: #add the left
    #                 queue.append(node.left)
    #             if node.right:#add the right
    #                 queue.append(node.right)
    #         level+=1 #if queue is there the level increase and obviously there 
    #         #would be pop but not append if no elements
    #         #start level is -0
    #     return level

    #DFS iterative - stack
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        depth,res=1,1 #if it has reached here , so root is there, length is min 1
        stack=[[root,depth]]
        while stack:
            node,depth=stack.pop() #pop values stack is like node|depth
            #that is how we are updating the value , see 38 line.
            if node: #why if node is because you can add the none/null in stack
            #through atack.append and the loop would be infinite.
                res=max(res,depth)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])
        return res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().maxDepth(root))