# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         # if len(nums)<3:
#         #     return []
#         nums.sort() #sort the nums
#         result=[] #to store
#         left_most=0 #first value
#         for i in range(1,len(nums)):
#             if i>1 and nums[i-1] == nums[i-2]:#curremt leftmost is 1step behind
#             #and we have to equate with last leftmost before current
#                 left_most+=1#move it 1 ahead
#                 continue
#             left=i #after leftmost
#             right=len(nums)-1 #last
#             while left<right: #compare till they coincide
#                 # if nums[left]==nums[left-1]: #already done
#                 #     continue
#                 sumof3=nums[left_most] + nums[left] + nums[right] #to check
#                 if sumof3 == 0:#valid condition
#                     result.append([nums[left_most],nums[left],nums[right]])#append to result
#                     left+=1 #move left and right to find new window
#                     right-=1
#                     while left<right and nums[left]==nums[left-1]:
#                     #this is if the same value of left in the left to right loop
#                         left+=1
#                     while left < right and nums[right] == nums[right+1]:

#                     #similarly this is if the same value of rgight in the left to right loop
#                         right -= 1
#                 elif sumof3<0:#sum is less increase left
#                     left+=1
#                     while left<right and nums[left]==nums[left-1]:
#                     #this is if the same value of left in the left to right loop
#                         left+=1
#                 else:
#                     right-=1
#                     while left < right and nums[right] == nums[right+1]:

#                     #similarly this is if the same value of rgight in the left to right loop
#                         right -= 1
#             left_most+=1#make the current value as leftmost
#         return result
# print(Solution().threeSum([-1,0,1,2,-1,4]))


# def maxArea(height) -> int:
#     if len(height)<1:
#         return 0
#     max_area=float("-inf")
#     left=0
#     right=len(height)-1
#     while left<right:
#         # print(left)
#         # print(right)
#         print(height[left],height[right],right-left)
#         area=min(height[left],height[right])*(right-left)
#         max_area=max(max_area,area)
#         print(area,max_area)
#         if height[left]<height[right]:
#             left+=1
#         else:
#             right-=1
#     return max_area

# print(maxArea(height = [1,8,6,2,5,4,8,3,7]))


# def myAtoi(self, s: str) -> int:
#     result = 0
#     sign = 1
#     iteration = 0
#     INT_MIN, INT_MAX = -2**31, 2**31 - 1 #rounding

#     def clamp(x):
#         return max(INT_MIN, min(INT_MAX, x))

#     for i in s:
#         if i == " " and iteration == 0: #ignore space only if its first, else the result would be returned before space.
#         # ex - "  -23" - gets into this loop and "-23 98" doesnt
#             continue
#         if i in "+-" and iteration == 0: #to capture the sign only if the sign is again in the first place
#             sign = -1 if i == "-" else 1
#             iteration += 1
#             continue
#         val = ord(i) - ord('0') #ord of the character being traversed
#         #- order of 0 , the value should lie between 0 and 9, if not then return the string so far.
#         if val < 0 or val > 9:
#             return clamp(result * sign)
#         iteration += 1#iteration 1 completes to handle space and -
#         result = result * 10 + val #3*10+2 = 32, 322 would be 32*10+2

#     return clamp(result * sign)
# print(myAtoi("42"))