
# from collections import deque

# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# #class Solution:
# def levelOrder(root):
#     if not root:
#         return []

#     result = []
#     queue = deque([root])

#     while queue:

#         level = []
#         level_size = len(queue)

#         for _ in range(level_size):

#             node = queue.popleft()

#             level.append(node.val)
#             print("1",queue)

#             if node.left:
#                 queue.append(node.left)
#                 print("2",queue)

#             if node.right:
#                 queue.append(node.right)
#                 print("3",queue)

#         result.append(level)

#     return result



# print(levelOrder(root))

#Input: root = [3,9,20,null,null,15,7]
#Output: [[3],[9,20],[15,7]]
#Every level should come in the seperate vector BFS
    #     3
    #    / \
    #   9   20
    #      /  \
    #     15   7

from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def levelOrder(root):
        if not root:#nothing in the tree
            return []
        result=[] #this is what we want to return
        queue=deque([root])
        #at first, the queue would be like list inside a list
        #[[3,9,20,None,None,15,7]] so 1 length at start
        while queue:#we will append the queue from right and pop elements from left so thats why deque - double ended queue
            level=[]#level i am at and collect those elements
            for i in range(len(queue)):
                node=queue.popleft() #atfirst nothing after this, now add elements
                level.append(node.val)#add the element , or say node to the level
                if node.left:#if i have left, i will add left to the queue
                #and again build the queue
                    queue.append(node.left)
                if node.right:#if i have right, i will then add right to the queu
                #and again again build the queue.
                    queue.append(node.right)
                # in second run the deque would be something like [[9],[20]] 
                #two elements, but in reality they are deque([TreeNode(9), #TreeNode(20)])
            result.append(level)#appending the elements of each level, one list with all the elements of the nodes
        return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(levelOrder(root))