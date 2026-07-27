# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         left=0
#         right=len(nums)-1
#         while left<right:
#             mid=(left+right)//2
#             if nums[mid]<nums[mid+1]:
#                 left=mid+1
#             else:
#                 right=mid
#         return left









#there can be multiple peak element but we have to return only one position
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left=0 #leftmost element
        right=len(nums)-1 #rightmost element
        while left <right:
            mid=(left+right)//2 #mid is middle, if 10.5 or 12.5 it will be 10 & 12
            print(mid,nums[mid])
            if nums[mid]<nums[mid+1]:#if mid+1 is smaller,expand left
                left=mid+1
            else:#mid is greater,squeeze right
                right=mid
        return left

sol=Solution()
print(sol.findPeakElement([1,2,1,3,5,6,4]))