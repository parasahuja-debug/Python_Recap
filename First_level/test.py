# class Solution:
#     def lengthOfLongestSubstring(self,s):
#         left=0
#         max_len=float("-inf")
#         dic={}
#         for right,value in enumerate(s):
#             if value in dic and dic[value] >= left: #partial correct with one addition
#                 left=dic[value]+1
#             dic[value]=right #save the value
#             max_len=max(max_len,right-left+1)
#         return max_len

# solution =Solution()
# print(solution.lengthOfLongestSubstring("abcbcacabp"))

# class Solution:
#     def findPeakElement(self,lis):
#         left=0
#         right=len(lis)-1
#         while left<right:
#             mid=(left+right)//2 #destination
#             if lis[mid]<lis[mid+1]:
#                 left=mid+1
#             else:
#                 right=mid
#         return left#loop would only end ehen left ==right, anything can be returned
#             # if lis[mid]>lis[mid-1] and lis[mid]>lis[mid+1]:
#             #     return lis[mid]
#             # elif lis[mid]<lis[mid-1]:
#             #     right=mid
#             # else:
#             #     left=mid+1

# sol=Solution()
# print(sol.findPeakElement([3,2,1]))

# def product_except_self(lis):

#     result_arr=[1]*len(lis)
#     prefix=1
#     for i in range(len(result_arr)):
#         result_arr[i]=prefix
#         prefix*=lis[i]
#         #[1,1,2,6]prefixarr
#         #[1,1,2,6]resultarr
#         #[24,12,4,1]suffixarr

#     suffix=1
#     for j in range(len(result_arr)-1,-1,-1):
#         result_arr[j]*=suffix
#         suffix*=lis[j]
#     return result_arr

# print(product_except_self([1,2,3,4]))

# class Solution:
#     def threeSum(self,nums):
#         nums.sort()
#         result=[]
#         for i in range(len(nums)-2):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             left=i+1
#             right=len(nums)-1
#             while left<right:
#                 sum1=nums[i]+nums[left]+nums[right]
#                 if nums[i]+nums[left]+nums[right]==0:
#                     result.append([nums[i],nums[left],nums[right]])
#                     left+=1
#                     right-=1
#                     while left < right and nums[left] == nums[left - 1]:
#                         left += 1

#                     while left < right and nums[right] == nums[right + 1]:
#                         right -= 1
#                 elif sum1<0:
#                     left+=1
#                 else:
#                     right-=1
#         return result


# solution=Solution()#object
# print(solution.threeSum([-1,0,1,2,-1,-4]))

# class Solution:
#     def twoSum(self,nums,target):
#         dic={}
        
#         for i in range(len(nums)):
#             target_val_in_dic=target-nums[i]
#             if target_val_in_dic in dic:
#                 return [dic[target_val_in_dic],i]
#             dic[nums[i]]=i
#         return -1



# sol=Solution() #object
# nums = [2, 7, 11, 15]
# target = 9
# result = sol.twoSum(nums, target)
# print(result)

# class Solution:
#     def isValid(self,s):
#         dic={'}':'{',']':'[',')':'('}
#         vec=[]
#         for i in s:
#             if i not in dic: #aapend if not there
#                 vec.append(i)
#             elif len(vec)==0:#it is there but vec is empty, cant pop
#                 return False
#             elif vec[len(vec)-1]==dic[i]:#it is there and is expected
#                 vec.pop()
#             else:
#                 return False

#         if len(vec)==0:
#             return True
#         else:
#             return False

# sol=Solution()#object
# s="([{}]"
# print(sol.isValid(s))

class Solution():
    def trap(self,nums):
        total=0
        left_max_arr=[0]*len(nums)
        right_max_arr=[0]*len(nums)

        left_max_arr[0]=nums[0]
        for i in range(1,len(left_max_arr)):
            left_max_arr[i]=max(left_max_arr[i-1],nums[i])
        
        right_max_arr[len(nums)-1]=nums[len(nums)-1]
        for j in range(len(right_max_arr)-2,-1,-1):
            right_max_arr[j]=max(right_max_arr[j+1],nums[j])

        for k in range(len(nums)):
            total+=min(left_max_arr[k],right_max_arr[k])-nums[k]
        
        return total

sol=Solution()
print(sol.trap([1,2,1,3,5,6,4]))