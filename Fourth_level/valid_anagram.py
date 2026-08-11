#anagram is if the two string can be formed from one another
# post rearranging alphabets and are of same length
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic={} #to save values from one string
        if len(s)!=len(t): #if length is not equal then obvious not anagram
            return False
        for right,val in enumerate(s):#save all values of one string
            dic[val]=dic.get(val,0)+1
        for right,val in enumerate(t):#now deduct the values if found in dic
            if val in dic:
                dic[val]-=1
            else:#if value is not in dic then obvious false
                return False
        if max(dic.values())>0:#for all the value if max of all dic value is greater than 0,
            #then false else true
            return False 
        else:
            return True

sol=Solution()
print(sol.isAnagram(s = "anagram", t = "nagaram"))
