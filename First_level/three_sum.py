# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         result=[]
#         nums.sort()
#         for i in range(len(nums)-2):
#             left=i+1
#             right=len(nums)-1
#             if i>0 and nums[i]==nums[i-1]:
#                 continue
#             # left=i+1
#             # right=len(nums)-1
#             while left<right:
#                 if nums[i]+nums[left]+nums[right]==0:
#                     result.append([nums[i],nums[left],nums[right]])
#                     while left<right and nums[left]==nums[left+1]:
#                         left+=1
#                     while left<right and nums[right]==nums[right-1]:
#                         right-=1
#                     left+=1
#                     right-=1
#                 elif nums[i]+nums[left]+nums[right]<0:
#                     left+=1
#                 else:
#                     right-=1
#         return result
                
            


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #mainly traverse the array
        #one value will start from 0
        #next is second and third is last
        #only on sorted array so that we skip the same combination
        #and increase left if less that 0 and decrease right if greater than 0
        #skip if the left and right are matching
        # i=0
        # j=i+1
        # k=n-1
        nums.sort()#sorted so that I can traverse unique triplets
        result=[]
        for i in range(len(nums)-2):#traverse before last 2 as j and k also would be there
            j=i+1#second element of array
            k=len(nums)-1 #last
            if i>0 and nums[i]==nums[i-1]:#same as old value skip
                continue
            while j<k: #traverse till i reach k
                sum1=nums[i]+nums[j]+nums[k]
                if sum1==0:#happy condition
                    result.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        #if j and j+1 are same
                        j+=1
                    while j<k and nums[k]==nums[k-1]:#if k and k-1 are same
                        k-=1
                    j+=1#move to next
                    k-=1#move to previous
                elif sum1<0:#j/left has to move
                    j+=1
                else:#k/right has to move
                    k-=1
        return result

solution=Solution()#object
print(solution.threeSum([-1,0,1,2,-1,-4]))