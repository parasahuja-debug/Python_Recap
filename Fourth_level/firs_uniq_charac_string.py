class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        for right,val in enumerate(s):#first store in a dic, the times character
            #came in a string
            dic[val]=dic.get(val,0)+1
        for right,val in enumerate(s):#then traverse to find if any character came
            #only once
            if dic[val]==1:#came only once
                return right#returned the location
        return -1
sol=Solution()
print(sol.firstUniqChar("leetcode"))