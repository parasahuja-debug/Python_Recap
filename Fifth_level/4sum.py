class Solution:
    def fourSum(self, nums, target: int):
        if len(nums)<4:
            return []
        nums.sort()
        # first_elem=0
        # second_elem=1 #[-2,-1,1,0,0,2] - target 0
        #-2,0,0,2
        #-2,-1,1,2   
        # left=second_elem+1
        result=[]
        # right=len(nums)-1
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            first_elem=i
            #[-2,-1]
            #[-1,1]
            for j in range(i+1,len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                # if j>0 and nums[j]==nums[j+1]:
                #     continue
                second_elem=j
                left=second_elem+1#[-2,-1,1,2] skip-2,-1,0,0
                right=len(nums)-1
                while left<right:
                    #print(first_elem,second_elem,left,right)
                    sum1=nums[first_elem]+nums[second_elem]+nums[left]+nums[right]
                    if sum1==target:
                        result.append([nums[first_elem],nums[second_elem],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
                    elif sum1<target:
                        left+=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                    else:
                        right-=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
        return result



