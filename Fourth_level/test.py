# class Solution:
#     def firstUniqChar(self,s):
#         dic={}
#         for index,value in enumerate(s): #O(n)
#             dic[value]=dic.get(value,0)+1 #store every character and increment by 1
#         for i in dic:#(O(m))
#             if dic[i]==1:
#                 return i
#         return -1



# sol=Solution()
# print(sol.firstUniqChar("eeoode"))

# class Solution:
#     def isAnagram(self,s,t):
#         dic={}
#         for i in s: # 0(n)
#             dic[i]=dic.get(i,0)+1 # this way we have all s in one location
#         for i in t:#O(m)
#             if i in dic:
#                 dic[i]=dic.get(i,0)-1
#             else:
#                 dic[i]=dic.get(i,0)+1
#         if max(dic.values())>0 or min(dic.values())<0:#O(1)=O(26) space
#             return dic,False
#         else:
#             return dic,True

        
# sol=Solution()
# print(sol.isAnagram(s = "anagram", t = "nagarame"))

# class Solution:
#     def groupAnagrams(self,listofstring):
#         dic={}
#         for string in listofstring:#timeO(n)
#             arrayofstring=[0]*26
#             for char in string:
#                 arrayofstring[ord(char)-ord('a')]+=1
#             arrayofstring=tuple(arrayofstring)
#             if arrayofstring in dic:
#                 dic[arrayofstring].append(string)
#             else:
#                 dic[arrayofstring]=[string]
#         return list(dic.values())#space O(1)
# # ans[[eat,tea,ate],[tan,nat],[bat]]


sol=Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))