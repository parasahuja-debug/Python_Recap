# class Solution:
#     def twoSum(self,arr1,k):
#         # for i in range(len(arr1)):
#         #     for j in range(i+1,len(arr1)):
#         #         if arr1[i]+arr1[j]==k:
#         #             return i,j
#         # return -1
#         dic={}
#         for index,value in enumerate(arr1):
#             target=k-value
#             if target in dic:
#                 return dic[target],index
#             dic[value]=index
#         return -1
class Solution:
    def twoSum(self,nums,target):
        left=0
        hash_store={}
        
        for right,value in enumerate(nums):
            target_exp=target-value
            if target_exp in hash_store:
                return [hash_store[target_exp],right]
            hash_store[value]=right
        return -1

sol=Solution() #object
nums = [2, 7, 11, 15]
target = 9
result = sol.twoSum(nums, target)
print(result)