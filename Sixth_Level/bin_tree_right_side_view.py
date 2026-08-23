class Solution:
    from collections import deque
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:#empty root condition
            return []
        capture_vec=[]#the right side view
        queue=deque([root])#deque because we need right side view, we will pop
        #fromleft
        while queue:
            for i in range(len(queue)):
                node=queue.popleft() #pop from left
                if node.left:
                    #capture_vec.append(node.val)
                    queue.append(node.left)#enter only when value is there
                if node.right:
                    # queue.append(node.left)
                    queue.append(node.right)#enter only when value is there
                #print(queue)
            if node:#last value insert
                capture_vec.append(node.val)
        return capture_vec

# [1] - 1
# [2,3] - 1,3
# [null,5,null,4] - 1,3,4
#so everytime it is the last element