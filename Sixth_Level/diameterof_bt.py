# diameter is number of edges, the max is what we have to return
# now, as per the question, diameter can be calculated through root and 
# can exists in left part or right part.
# for values through root, can we say , height of left + height of right= diameter
# and the same application would happen in right or left subtree, the diameter would 
# go from any root in left subtree or right subtree.
#so max of either 3 would give the diameter
class Solution:
    def diameterOfBinaryTree(self, root):

        def height(node):
            if not node:
                return 0

            return 1 + max(height(node.left), height(node.right))

        def diameter(node):
            if not node:
                return 0

            left_diameter = diameter(node.left)
            right_diameter = diameter(node.right)

            left_height = height(node.left)
            right_height = height(node.right)

            return max(
                left_diameter,
                right_diameter,
                left_height + right_height
            )

        return diameter(root)#call diameter(starts)