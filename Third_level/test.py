# class Solution:
#     def maxSubArray(self,nums):
#         cal_sum=0
#         max_sum=float("-inf")
#         for i in range(len(nums)):
#             cal_sum+=nums[i]
#             max_sum=max(max_sum,cal_sum)
#             if cal_sum<0:
#                 cal_sum=0
#         return max_sum
#kadane's algo
# -2 , -2, 0
# 1,1,1
# -2,1,0
# 4,4,4
# 3,4,3
# 5,5,5
# 6,6,6
# 1,6,1

# class Solution:
#     def maxProfit(self,nums):
#         buy_at=nums[0]
#         max_prof=0
#         for i in range(1, len(nums)):
#             if nums[i]<buy_at:
#                 buy_at=nums[i]
#             max_prof=max(max_prof,nums[i]-buy_at)
#         return max_prof

# #2 <1
# #1-1 =0, 0
# #2,2
# #3,3
# #0,0
# #1,3
# #1,
# In House Robber, you need to calculate:
# The maximum amount of money you can rob without robbing two adjacent houses.

# class Solution:
#     def rob(self,nums):
#         #making the same array to have the house robbery sum and returning the last
#         #value of the array
#         if not nums:
#             return 0
#         if len(nums)==1:
#             nums[0]=nums[0]
        
#         nums[1]= max(nums[0],nums[1])
#         for i in range(2,len(nums)):
#             nums[i]=max(nums[i]+nums[i-2],nums[i-1])
            
#         return nums[-1]
#         #
#         # return amount    
# # if lets say 2 only then 2
# # if lets say 7 then 7
# # start with 3rd element, 


# #for n n+1 and n-1 are not there.
# #for n not there , n+1 and n-1 to consider.

# sol=Solution()
# print(sol.rob([2, 7, 9, 3, 1]))


# sol=Solution()
# print(sol.rob([2,1,3,4,1,2,1,5,4]))
#How many distinct ways can you reach the top of n stairs 
# if you can climb either 1 step or 2 steps at a time?
class Solution:
    def climbStairs(self,n):
        if n==0:
            return 0
        nums=[0]*n
        nums[0]=1
        if n>1:
            nums[1]=2
        for i in range(2,n):
            nums[i]=nums[i-1]+nums[i-2]
        return nums[-1]

# 1 - 1
# 2 - 2
# 3 - 2+1,1+1+1,1+2
# 4 - 2+2,1+2+1,1+1+1+1,1+1+2,2+1+1
        
#         nums[1]=
#         nums[]

sol=Solution()
print(sol.climbStairs(4))