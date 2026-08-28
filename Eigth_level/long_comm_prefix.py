# Write a function to find the longest common prefix string 
# amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0: #the word string is all empty
            return ""
        if len(strs)==1: #f there is only one word
            return strs[0]
        prefix=""#find the prefix here
        first_char=0#to determine the length of prefix, it is used for implement
        for i in range(len(strs[0])):
            #for first word, you can compare with first word only
            for j in range(len(strs)):#with all the words including self
                if len(strs[j])==first_char:#if any word length is less
                    return prefix
                #print("j",j," and ",strs[j][first_char])
                if strs[0][i]==strs[j][first_char]:#first char of word you are
                    #comparing with the words character you are comparing
                    continue#if found continue with other words
                return prefix#return prefix if character is not same
            first_char+=1#length for 31 line mainly and 28 line
            prefix=prefix+strs[0][i]#prefix addition
            # print(prefix," firs",first_char)
        return prefix
        
        # for i in range(strs):
        #     # for j in range(0,len(strs[i]):
        #     left=0
        #     while len(strs[i]):
        #         if strs[left][j]==strs[i][j]