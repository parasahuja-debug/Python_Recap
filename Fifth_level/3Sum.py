# again we have - nums[i],nums[j],nums[k]
# i != j, i != k, and j != k, - this means we have to keep the pointers seperate
# nums[i] + nums[j] + nums[k] == 0.
# no duplicate triplets, meaning if -1 is traversed, it should not be traversed

# [-1,0,1,2,-1,-4]
# sort the value - [-4,-1,-1,0,1,2]
# ok start with first - -4
# first of all - len() is not 3
# iterate from 1st
# -1 - left, 2 is right
# left- increase on small and right- decrease om large
# -4+(-1)+(2)=-3 increase left
# -1 again skip
# -4+0+2- increase
# no pair
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums)<3:
            return []
        nums.sort() #sort the nums
        result=[] #to store
        left_most=nums[0] #first value
        for i in range(1,len(nums)):
            if i>1 and nums[i-1] == nums[i-2]:#curremt leftmost is 1step behind
            #and we have to equate with last leftmost before current
                left_most=nums[i]#move it 1 ahead
                continue
            left=i #after leftmost
            right=len(nums)-1 #last
            while left<right: #compare till they coincide
                # if nums[left]==nums[left-1]: #already done
                #     continue
                sumof3=left_most + nums[left] + nums[right] #to check
                if sumof3 == 0:#valid condition
                    result.append([left_most,nums[left],nums[right]])#append to result
                    left+=1 #move left and right to find new window
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                    #this is if the same value of left in the left to right loop
                        left+=1
                    while left < right and nums[right] == nums[right+1]:

                    #similarly this is if the same value of rgight in the left to right loop
                        right -= 1
                elif sumof3<0:#sum is less increase left
                    left+=1
                else:
                    right-=1
            left_most=nums[i]#make the current value as leftmost
        return result
        
      

