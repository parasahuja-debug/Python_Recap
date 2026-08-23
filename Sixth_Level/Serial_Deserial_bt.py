def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        vectorr=[] #to store
        def vectorr_append(root):#called for root for the first time
            if not root:
                vectorr.append("None")#calling no node as None
                return
            vectorr.append(str(root.val)) #appending the root value first #Preorder
            left=vectorr_append(root.left)#then append the left by calling func agai
            right=vectorr_append(root.right)#then append the right
            #once all are appended the value is returned
            
        vectorr_append(root) #something because we have to append all values first
        #we would have done similar way if we had to find the max or min
        return ",".join(vectorr) #"1,2,3,4,5,6,7,8" value something like this
    #converted into str of values

def deserialize(self, data):
    values = data.split(",") #stringspli made to vector
    index = 0 #start from index 0 nd start adding

    def data_des():
        nonlocal index #this is to specify the index is non local

        if values[index] == "None": #first none chaeck and return none
            index += 1#move to next value
            return None

        node = TreeNode(int(values[index])) #include the value in tree 
        index += 1 #increase the value

        node.left = data_des() #insert the left to treenode
        node.right = data_des()#insert the right to treenode

        return node #return the tree

    return data_des()