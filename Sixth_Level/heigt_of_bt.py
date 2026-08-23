def height(node):
            if not node:
                return 0

            return 1 + max(height(node.left), height(node.right))
#1 for the current node as the not node condition is passed
#repeat the same for left and right and sum the max value ,
#imagine the left or right as the original tree only