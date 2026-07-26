class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}#store the positon of elements
        left=0#start from left most
        max_len=0#maxlength sofar calculation
        for index,value in enumerate(s):
            if value in dic and dic[value]>=left:
                left=dic[value]+1#increase left by 1 and then calculate the max 
                #length, only in two cases, 
                # when i have already seen the element(valuein dic) 
                # and the element's position that i have seen(dic[value]) 
                # is greater than or equal to current left
            dic[value]=index#store index position of value
            max_len=max(max_len,index-left+1)#right-left+1
        return max_len,s[left:left+max_len]

solution =Solution()
print(solution.lengthOfLongestSubstring("ahjgsdukasghdjou"))




# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         last_seen = {}#tokeep a tab of which letter i have seen so far
#         left = 0#start from left most
#         max_len = 0#max_len0 to compare

#         for right in range(len(s)):
#             if s[right] in last_seen and last_seen[s[right]] >= left:#if right element is same as left or i have already seen it in the string and the position of right(stored) is greater than left 
#                 left = last_seen[s[right]] + 1

#             last_seen[s[right]] = right
#             max_len = max(max_len, right - left + 1)

#         return max_len



