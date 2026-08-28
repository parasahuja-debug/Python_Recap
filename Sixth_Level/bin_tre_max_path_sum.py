class Solution:
    def maxPathSum(self, root):

        max_sum = float("-inf")

        def dfs(node):

            nonlocal max_sum

            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            max_sum = max(max_sum, node.val + left + right)#this needs to be calculate
            #d for each tress with left and right 

            return node.val + max(left, right) #this is returned , lets imagine
        #root of left/right also have left and right, 
        # and we are stating that we need a path
        #so the root also needs to know the path down the line
        #so it would be the rootnode +left or right node whichever is high

        dfs(root)

        return max_sum