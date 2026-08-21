# the problem ask for location of the first character in the string 'leetcode'
# not in the dictionary the element is saved.
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
    #space is o(n) because the elements, characters are limited (26).
    #O(26)= O(1) eventually.
    #Always remember it is not storage , it is operation time, stoorage in dictionary
    # would be O(n) only
sol=Solution()
print(sol.firstUniqChar("leetcode"))