class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        find=0
        for i in nums:
            find=find^i
        return find
    #x^x=1 and x^0=x