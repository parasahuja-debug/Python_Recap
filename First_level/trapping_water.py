# def trap(nums):
#     left_max_vec=[0] * len(nums)
#     right_max_vec=[0] * len(nums)
#     total_vol=0
#     #if we fill out these vectors we will know which is largest on right
#     #which is largest on left during the vector

#     left_max_vec[0]=nums[0] #first height is as is
#     for i in range(1,len(nums)):
#         left_max_vec[i]=max(left_max_vec[i-1],nums[i]) #current and previous
#     #left_max_vec=[4,4,4,4,4,5] fill from left to right

#     right_max_vec[len(nums)-1]=nums[len(nums)-1] #last height is as is
#     for j in range(len(nums)-2,-1,-1): #from,end,step, -2 is because last height is already
#         #stored in 13th line
#         right_max_vec[j]=max(right_max_vec[j+1],nums[j])
    
#     #right_max_vec=[5,5,5,5,5,5] fill from right to left
#     for k in range(len(nums)):
#         total_vol+=min(left_max_vec[k],right_max_vec[k])-nums[k]
    
#     return total_vol



# print(trap(nums = [4,2,0,3,2,5]))




class Solution:
    def trap(self, height: List[int]) -> int:
        #between the towers we have to calculate and sum the amount
        #of water stored between each tower
        #calculate the left max array and right max array
        #why because the amount stored is min of (max of left and right) minus the height
        # so three loops one for left max and one for right max
        # for which first (left max) and last of(right max) would be the same
        #height as of the array 
        # and then we will finc max of both and minus the height of current in 
        #lst loop
        left_max_arr=[0]*len(height)
        right_max_arr=[0]*len(height)
        total_vol=0
        left_max_arr[0]=height[0]
        for i in range(1,len(left_max_arr)):
            left_max_arr[i]=max(left_max_arr[i-1],height[i])
        
        right_max_arr[len(right_max_arr)-1]=height[len(right_max_arr)-1]
        for j in range(len(right_max_arr)-2,-1,-1):
            right_max_arr[j]=max(right_max_arr[j+1],height[j])
        
        for k in range(len(right_max_arr)):
            total_vol+=min(left_max_arr[k],right_max_arr[k])-height[k]
        return total_vol

sol=Solution()
print(sol.trap([1,2,1,3,5,6,4]))