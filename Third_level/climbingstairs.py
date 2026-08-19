#How many distinct ways can you reach the top of n stairs 
# if you can climb either 1 step or 2 steps at a time?
class Solution:
    def climbStairs(self, n: int) -> int:
        #tabulization solution
        #meaning bottom to top approach where smallest is calculated first
        #smallest is given
        if n<=1:
            return 1
        result=0
        prev1= 1 #0th element
        prev2= 1 #1st element
        #basically fn= fn-1 + fn-2
        for i in range(2,n+1):
            result=prev1+prev2
            #make last as second last #0th
            prev1=prev2
            #make secondlast as last
            prev2=result
        return result

sol=Solution()
print(sol.climbStairs(2))