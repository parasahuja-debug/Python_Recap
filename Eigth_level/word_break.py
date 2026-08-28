# Problem: Given a string s and a dictionary of words, determine 
# if s can be segmented into a space-separated sequence of dictionary words.
# s = "applepie" → a-p-p-l-e-p-i-e (indices 0 to 8)

# dict = {"app", "le", "apple", "pie"}
def wordBreak(s, wordDict):
    words = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1): #traverse through n+1
        for j in range(i):#j would only run till i but multiple times starting from 0
            if dp[j] and s[j:i] in words: #if aaa is traced then aaaa would also be
                #traces via s[j:i]
                dp[i] = True
                break#break from the loop if for that location true is found
    
    return dp[n]#display only the last, if true converted then true else false

# I tried but failed in "aaaaaaa" and word dict - ["aaa","aaaa"]
# from my code last a would be left and hence false
# left =0
# vector=[]
# for char,val in enumerate(s):
#     if s[left:char+1] in wordDict:
#         print("found 1",s[left:char+1])
#         left=char+1
#         if char==len(s)-1:
#             return True
# return False