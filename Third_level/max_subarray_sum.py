# this is kadane's algo,and greedy approach
#we want the highest sum of subarray, meaning we have to traverse to right
#and find the sum of the subarray, and return the max
class Solution:
    def maxSubArray(self, nums) -> int:
        #initiate current sum as 0
        curr_sum=0
        #Max_sum as minus infinity 
        max_sum=float("-inf")
        for i in range(len(nums)):
            #we are starting to add values of the nums array to current sum
            curr_sum=nums[i]+curr_sum
            #take max out of the value, max_sum or current value
            max_sum=max(max_sum,curr_sum)
            #acc to kadane's algo, if the sum is less than 0 lets start fresh,
            #so initialising the values by 0, and then again repeat the process.
            
            if curr_sum<0:
                curr_sum=0
        return max_sum

sol=Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))