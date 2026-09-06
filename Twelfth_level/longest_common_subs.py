# Given two strings text1 and text2,
# return the length of their longest common subsequence. 
# If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string 
# with some characters (can be none) deleted without changing the 
# relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is 
# common to both strings.

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  

# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         if len(text1)==0 or len(text2)==0:
#             return 0
#         memo={}
#         # max_length=0
#         # i=0
#         def dp(text1,text2):
#             #nonlocal max_length
#             if len(text1)==0 or len(text2)==0:
#                 return 0
#             if (text1,text2) in memo:
#                 return memo[(text1,text2)]
#             if text1[0]==text2[0]:
#                 # max_length+=1
#                 result=1 + dp(text1[1:],text2[1:])
#             else:
#                 select=dp(text1,text2[1:])
#                 deselect=dp(text1[1:],text2)
#                 result=max(select,deselect)
#             memo[text1,text2]=result
#             return result


#         return dp(text1,text2)
#         #return max_length

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                result = 1 + dp(i + 1, j + 1)
            else:
                select = dp(i, j + 1)
                deselect = dp(i + 1, j)
                result = max(select, deselect)

            memo[(i, j)] = result
            return result

        return dp(0, 0)