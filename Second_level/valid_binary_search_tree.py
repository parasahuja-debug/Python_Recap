#problem statement , left side is less than root and right side is greater than root
#even the nodes of left node from root, the value should not exceed rooot.
#vice-a-versa for right node, value should be greater
#now can we say root lies - (-infinity, root, infinity)
#and left should not be greater than root so - (-infinity,value,root)
#and right should be greater than root so - (root,value,infinity)

#for every nodes of nodes there can be atmost two nodes and same thing is to be
#checked, so recursion
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().isValidBST(root))