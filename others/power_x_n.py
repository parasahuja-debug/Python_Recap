class Solution:
    def myPow(self, x: float, n: int) -> float:
        #return x ** n
       
        result=1
        isngeative=False
        if n<0:
            n=-n
            isngeative=True
        for i in range(n):
            result*=x
        if isngeative:
            return 1/result
        else:
            return result