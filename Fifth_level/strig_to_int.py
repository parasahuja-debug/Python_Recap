# class Solution:
#     def myAtoi(self, s: str) -> int:
#         result=0
#         sign=1
#         iteration=0
#         for i in s:
#             if i==" " and iteration==0:
#                 continue
#             if i in "+-" and iteration==0:
#                 if i=="-" : 
#                     sign=-1
#                 else:
#                     sign=+1
#                 iteration += 1
#                 continue
#             val=ord(i)-ord('0')
#             if val<0 or val>9:
#                 if result!=0:
#                     return result*sign #missed here.
#                 else:
#                     return 0
#             iteration+=1
#             result=result*10+val
#         result *= sign
#         INT_MIN, INT_MAX = -2**31, 2**31 - 1
#         return max(INT_MIN, min(INT_MAX, result))

#string to integer but with two conditions
#if there are spaces first ignore the spaces
#consider the signs
#traverse only til the numbers, and if anythig except that comes , return the 
#number traversed so far
class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        sign = 1
        iteration = 0
        INT_MIN, INT_MAX = -2**31, 2**31 - 1 #rounding

        def clamp(x):
            return max(INT_MIN, min(INT_MAX, x))

        for i in s:
            if i == " " and iteration == 0: #ignore space only if its first, else the result would be returned before space.
            # ex - "  -23" - gets into this loop and "-23 98" doesnt
                continue
            if i in "+-" and iteration == 0: #to capture the sign only if the sign is again in the first place
                sign = -1 if i == "-" else 1
                iteration += 1
                continue
            val = ord(i) - ord('0') #ord of the character being traversed
            #- order of 0 , the value should lie between 0 and 9, if not then return the string so far.
            if val < 0 or val > 9:
                return clamp(result * sign)
            iteration += 1#iteration 1 completes to handle space and -
            result = result * 10 + val #3*10+2 = 32, 322 would be 32*10+2

        return clamp(result * sign)