class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        req=None
        count=0
        for i in nums:
            if req==None:
                req=i
                count+=1
            elif i==req:
                count+=1
            else:
                if count==1:
                    count=0
                    req=None
                else:
                    count-=1
        return req