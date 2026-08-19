# In House Robber, you need to calculate:
# The maximum amount of money you can rob without robbing two adjacent houses.
class Solution:
    def rob(self, nums) -> int:
        #initialise which is the second point of dp
        dp=[0]*len(nums) #arrayto store the data
        #first initialization
        dp[0]=nums[0] #if i have an array of 1, then first value is whre the 
        #robbery would happen
        #second initialization
        if len(nums)>1:#just in case length is more than 0
            dp[1]=max(nums[0],nums[1])#we have to rob and get highest robbery
        #also, we cannot rob the adjacent
        #so for two element vector/2 houses, whosover has the highest we
        #will rob that house
        
        #now for other elements
        for i in range(2,len(nums)):#start with 3, as 2 is already known
            #print(dp)
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
            #what we did is if i am on 3rd, i cant add 2nd but only add 1st
            # we know dp[i-2] which is 0th element/1st element
            # and similarly, if i do not chose 3rd, then i will only have 2nd
            # so max out of both would give me highest figure

            #save all data in dp array/result array and store the max in the array
            #the last element would give the highest robbery
        return dp[len(nums)-1]

sol=Solution()
print(sol.rob([2,1,3,4,1,2,1,5,4]))