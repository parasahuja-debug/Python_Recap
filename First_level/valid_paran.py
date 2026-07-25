class Solution:
    def isValid(self, s: str) -> bool:
        # previous=-1
        # while previous!=len(s):
        #     previous=len(s)
        #     s=s.replace("()","").replace("[]","").replace("{}","")
        
        # if s=="":
        #     return True
        # else:
        #     return False
    
        store=[]
        arra={')':'(','}':'{',']':'['}
        for i in s:
            if i in arra:#closing brackets found
                print("enter if")
                top=store.pop() if store else "#"
                print(top)
                if top!=arra[i]:
                    return False
            else:#store value
                print("enter else")
                store.append(i)
        return not store
             



class Solution:
    def isValid(self, s: str) -> bool:
        #lets say i save the first one
        closing={')':'(',']':'[','}':'{'}
        store_tocheck=[]
        for i in s: #traverse through the loop
            if i in closing:#i is a closing bracket whose #value exists in hash
                if len(store_tocheck)==0:#i do not have #anything in store or you can say
                #no opening exists 
                    return False
                elif closing[i]==store_tocheck[len(store_tocheck)-1]:#closing bracket value
                #i.e opening is last element of the store
                #which is valid
                    store_tocheck.pop()#lets make it empty
                else:#if the closing value is not the last #value of the store
                    return False
            else:#it is the opening bracket
                store_tocheck.append(i)
        if len(store_tocheck)==0:
            return True
        else:
            return False

sol=Solution()#object
s="([{}])"
print(sol.isValid(s))