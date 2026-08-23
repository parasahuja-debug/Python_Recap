#if path sum is equal to targetsum then return true
#if reaching till leaf , the target matches return true
#if the value matches somewhere in middle , ans is false
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # if root.val==targetSum:
        #     return True
        curr_sum=0 #find the current sum
        def find_target(root,target,curr_sum):
            if not root:
                return False

            curr_sum+=root.val #add the root value and traverse left
            
            if curr_sum==target and not root.left and not root.right: #if sum is found
                #and the current node is leaf node then true
                return True
            
            left=find_target(root.left,target,curr_sum)#find for left
            right=find_target(root.right,target,curr_sum)#find for right
            return left or right #if either true then true
            
        return find_target(root,targetSum,curr_sum)
