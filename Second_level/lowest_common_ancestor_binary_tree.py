# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        #what we will do is traverese the left portion of the tree and
        #lets find the p and q ,
        #and that would be possible if p or q equals root
        #this is -(where we allow a node to be a descendant of itself).”
        #meaning node would be ancestor of itself.

        #if we have 6 and 0, we need to find the element under whose branch both 
        #exists, that should be lowest possible - 6 has 6,5 and 3,,, 0 has 0,1,3
        #3 is the lowest.
        #take 0 and 8, p and q, 0 has 0,1,3 and 8 has 8,1,3. but least is 1.

        if not root:
            return root
        
        if p==root or q==root:
            return root #you are your own ancestor
        
        left_anc=Solution().lowestCommonAncestor(root.left,p,q) #find the left most anc 3, goes to 5 then 6 then null.
        #eventually we would return null from this branch or anc from 24,25 line
        #or 21 line
        right_anc=Solution().lowestCommonAncestor(root.right,p,q)#find the right most anc 5 has right, 2, but 2 has left, then 2 would look onto its right 4.
        #eventually we would return null from this branch or anc from 24,25 line
        #or 21 line

        if left_anc and right_anc:#both not null
            return root #ans
        elif left_anc:#left is not null but right is, hence an ancestor
            return left_anc
        else:
            return right_anc#left is null or both left and right is ancestor , both conditions

#sol works in leetcode - 
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)

# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# print(Solution().lowestCommonAncestor(root,9,7))